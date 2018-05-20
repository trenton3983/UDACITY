"""This method is the same as Lesson 13 Question 10 in the Jupyter Notebook Lesson_8-13.ipynb
The program is used to audit the osm to gather the street types that require mapping to long form
names.  The output of the file is visually examined and appropriate abbreviated street types are
manually added to MAPPING.

This file does not update the OSM or the csv file, it's strictly used for information gathering.
"""

import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint


saved_street_names_audit = 'C:/PythonProjects/UDACITY/01_Data_Analyst/03_Data_Wrangling/audited_street_names_full.txt'

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

EXPECTED = ['Street', 'Avenue', 'Boulevard', 'Drive', 'Court', 'Place', 'Square', 'Lane', 'Road',
            'Parkway', 'Commons', 'Highway', 'Loop', 'Terrace', 'Trail', 'Way', 'North', 'South',
            'West', 'East', 'Circle', 'Broadway', 'Path', 'View']

MAPPING = {"St": "Street", "St.": "Street", "street": "Street", "st.": "Street",
           "Ave": "Avenue", "Ave.": "Avenue", "AVE": "Avenue",
           "Rd.": "Road", "Rd": "Road", "Rode": "Road",
           "Dr": "Drive", "Dr.": "Drive", "Srive": "Drive",
           "Blvd": "Boulevard", "Ln": "Lane", "Blvd.": "Boulevard",
           "TRL": "Trail", "Hwy": "Highway",
           "Pky": "Parkway", "Pkwy": "Parkway",
           "GLN": "Glen", "Cir": "Circle", "Ct.": "Court",
           "NW": "Northwest", "NE": "Northeast", "SE": "Southeast", "SW": "Southwest",
           "northeast": "Northeast", "N.": "North"}


def audit_street_type(street_types, street_name, expected=EXPECTED):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    """
    Receives <tag and returns True if ['k'] == 'addr:street', else False
    :param elem:
        <tag k="addr:street" v="Northwest 23rd Avenue" />
    :return:
        True or False
    """
    return elem.attrib['k'] == "addr:street"


def audit(osmfile):
    osm_file = open(osmfile, "rb")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types


def update_name(name, mapping=MAPPING):
    """
    Splits tag.attrib['v'] and checks each string against MAPPING.
    If there's a value match, the string is changed to the new value.
    Args:
        name (str): "NW 23rd Ave"
        mapping (dict): {"Ave": "Avenue"}
    Returns:
        name (str): 'Northwest 23rd Avenue
    """
    name = name.strip()
    print(f'This is name: {name}')
    x = name.split()
    print(f'This is x: {x}')
    for y in x:
        if y in mapping:
            name = name.replace(y, mapping[y])
    return name


def main(filename):
    """Prints a nested dict of potentially problematic street types """
    with open(saved_street_names_audit, 'w+') as f:
        st_types = audit(filename)
        pprint.pprint(dict(st_types))

        for st_type, ways in st_types.items():
            print(f'Street Type: {st_type}\nWays: {ways}')
            for name in ways:
                better_name = update_name(name)
                test = f'{name} => {better_name}\n'
                print(test)
                f.write(test)
            print('\n')

    f.close()


if __name__ == '__main__':

    osm_portland = 'C:/PythonProjects/UDACITY/01_Data_Analyst/03_Data_Wrangling/Data Wrangling ' \
                   'Project/portland_oregon_50_sample.osm'
    osm_portland_full = 'C:/PythonProjects/UDACITY/01_Data_Analyst/03_Data_Wrangling/Data Wrangling ' \
                        'Project/portland_oregon.osm'

    main(osm_portland_full)