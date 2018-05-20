"""This program takes the osm data, then shapes nodes, nodes_tags, ways, ways_nodes and ways_tags into
the correct format, fixes, street name, zip codes and city name and writes the information to a csv file."""

import codecs
import pprint
import re
import xml.etree.cElementTree as ET

import cerberus
import unicodecsv as csv
from project_fix_city_name import fix_city_name
from project_fix_street_name import fix_street_name
from project_fix_zip_code import fix_zip_codes

import schema

OSM_PATH = "example.osm"

NODES_PATH = "nodes.csv"
NODE_TAGS_PATH = "nodes_tags.csv"
WAYS_PATH = "ways.csv"
WAY_NODES_PATH = "ways_nodes.csv"
WAY_TAGS_PATH = "ways_tags.csv"

LOWER_COLON = re.compile(r'^([a-z]|_)+:([a-z]|_)+')
PROBLEM_CHARS = re.compile(r'[=+/&<>;\'"?%#$@,. \t\r\n]')

SCHEMA = schema.schema

# Make sure the fields order in the csvs matches the column order in the sql table schema
NODE_FIELDS = ['id', 'lat', 'lon', 'user', 'uid', 'version', 'changeset', 'timestamp']
NODE_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAY_FIELDS = ['id', 'user', 'uid', 'version', 'changeset', 'timestamp']
WAY_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAY_NODES_FIELDS = ['id', 'node_id', 'position']


def get_tags(element):
    """Manages tags for node_tags and way_tags.  Splits the tag and assigns a value
    to the appropriate key.  This is also where tag values are repaired prior to
    writing them into the csv."""
    tags = []
    for tag in element.iter('tag'):

        if PROBLEM_CHARS.match(tag.attrib['k']):
            continue
        else:
            k_split = (tag.attrib['k']).split(':', 1)
            if len(k_split) == 1:
                key = k_split[0]
                type_ = 'regular'
            else:
                key = k_split[1]
                type_ = k_split[0]

            # Repair Street Name to a Long Form (i.e. NW to Northwest)
            if type_ == 'addr' and key == 'street':
                tag.attrib['v'] = fix_street_name(tag.attrib['v'])

            # Repair Zip Codes to 5 digits
            if type_ == 'addr' and key == 'postcode':
                tag.attrib['v'] = fix_zip_codes(tag.attrib['v'])

            # Repair City Names
            if type_ == 'addr' and key == 'city':
                tag.attrib['v'] = fix_city_name(tag.attrib['v'])

            tags.append({'id': element.attrib['id'],
                         'key': key,
                         'value': tag.attrib['v'],
                         'type': type_})
    return tags


def shape_element(element, node_attr_fields=NODE_FIELDS, way_attr_fields=WAY_FIELDS):
    """Clean and shape node or way XML element to Python dict"""

    node_attribs = {}
    way_attribs = {}
    way_nodes = []

    if element.tag == 'node':

        for field in node_attr_fields:
            node_attribs[field] = element.attrib[field]

        return {'node': node_attribs, 'node_tags': get_tags(element)}

    elif element.tag == 'way':

        for field in way_attr_fields:
            way_attribs[field] = element.attrib[field]

        for i, nodes in enumerate(element.iter('nd')):
            way_nodes.append({'id': way_attribs['id'],
                              'node_id': nodes.attrib['ref'],
                              'position': i})

        return {'way': way_attribs, 'way_nodes': way_nodes, 'way_tags': get_tags(element)}


# ================================================== #
#               Helper Functions                     #
# ================================================== #
def get_element(osm_file, tags=('node', 'way', 'relation')):
    """Yield element if it is the right type of tag"""

    context = ET.iterparse(osm_file, events=('start', 'end'))
    _, root = next(context)
    for event, elem in context:
        if event == 'end' and elem.tag in tags:
            yield elem
            root.clear()


def validate_element(element, validator, schema=SCHEMA):
    """Raise ValidationError if element does not match schema"""
    if validator.validate(element, schema) is not True:
        field, errors = next(validator.errors.item())
        message_string = "\nElement of type '{0}' has the following errors:\n{1}"
        error_string = pprint.pformat(errors)

        raise Exception(message_string.format(field, error_string))


# ================================================== #
#               Main Function                        #
# ================================================== #
def process_map(file_in, validate):
    """Iteratively process each XML element and write to csv(s)"""

    with codecs.open(NODES_PATH, 'wb') as nodes_file, \
            codecs.open(NODE_TAGS_PATH, 'wb') as nodes_tags_file, \
            codecs.open(WAYS_PATH, 'wb') as ways_file, \
            codecs.open(WAY_NODES_PATH, 'wb') as way_nodes_file, \
            codecs.open(WAY_TAGS_PATH, 'wb') as way_tags_file:

        nodes_writer = csv.DictWriter(nodes_file, NODE_FIELDS)
        node_tags_writer = csv.DictWriter(nodes_tags_file, NODE_TAGS_FIELDS)
        ways_writer = csv.DictWriter(ways_file, WAY_FIELDS)
        way_nodes_writer = csv.DictWriter(way_nodes_file, WAY_NODES_FIELDS)
        way_tags_writer = csv.DictWriter(way_tags_file, WAY_TAGS_FIELDS)

        nodes_writer.writeheader()
        node_tags_writer.writeheader()
        ways_writer.writeheader()
        way_nodes_writer.writeheader()
        way_tags_writer.writeheader()

        validator = cerberus.Validator()

        for element in get_element(file_in, tags=('node', 'way')):
            el = shape_element(element)
            if el:
                print(el)
                if validate is True:
                    validate_element(el, validator)

                if element.tag == 'node':
                    nodes_writer.writerow(el['node'])
                    node_tags_writer.writerows(el['node_tags'])
                elif element.tag == 'way':
                    ways_writer.writerow(el['way'])
                    way_nodes_writer.writerows(el['way_nodes'])
                    way_tags_writer.writerows(el['way_tags'])


if __name__ == '__main__':
    # Note: Validation is ~ 10X slower. For the project consider using a small
    # sample of the map when validating.
    filename = 'D:/PythonProjects/UDACITY/01_Data_Analyst/03_Data_Wrangling/Data Wrangling ' \
               'Project/portland_oregon.osm'

    filename2 = 'E:/Users/Trenton J. McKinney/PycharmProjects/UDACITY/01_Data_Analyst/03_Data_Wrangling/Data ' \
                'Wrangling Project/portland_oregon.osm'

    process_map(filename2, validate=True)