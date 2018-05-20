"""This method is similar to Lesson 13 Question 10 in the Jupyter Notebook Lesson_8-13.ipynb
The program is used to audit the osm to gather the city names that require mapping to corrected forms.
The output of the file is visually examined and appropriate city names are manually added to MAPPING.

This file can be used to audit the osm file or the method fix_city_name can be imported to fix the
city name prior to writing the csv file.
"""

import xml.etree.cElementTree as ET
from collections import defaultdict
import pprint


MAPPING = {"molalla": "Molalla",
           "portland": "Portland",
           "vancouver": "Vancouver",
           "97086": "Happy Valley",
           "Portland, OR": "Portland",
           "Portland, Oregon": "Portland",
           "Beaverton, OR": "Beaverton",
           "vernonia": "Vernonia",
           "OR": ""
           }


def audit_city_type(city_types, city_name):
    city_types[city_name].add(city_name)


def is_city_name(elem):
    """
    Receives <tag and returns True if ['k'] == 'addr:city', else False
    :param elem:
        <tag k="addr:city" v="Portland" />
    :return:
        True or False
    """
    return elem.attrib['k'] == "addr:city"


def audit(osmfile):
    osm_file = open(osmfile, "rb")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_city_name(tag):
                    audit_city_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types


def fix_city_name(name, mapping=MAPPING):
    """
    Splits tag.attrib['v'] and checks each string against MAPPING.
    If there's a value match, the string is changed to the new value.
    :param name:
        (str) - 'portland'
    :param mapping:
        (dict) - {'portland': 'Portland'}
    :return:
        (str) - 'Portland'
    """

    if name in mapping:
        name = name.replace(name, mapping[name])
    return name


def main(filename):
    """Prints a nested dict of potentially problematic city names"""
    st_types = audit(filename)
    # pprint.pprint(dict(st_types))

    for st_type, ways in st_types.items():
        for name in ways:
            better_name = fix_city_name(name)
            print(name, "=>", better_name)


def test(name):

    new_name = fix_city_name(name)
    print(name, "=>", new_name)

    if name == 'molalla':
        assert new_name == 'Molalla'
    if name == 'OR':
        assert new_name == ''
    if name == 'vancouver':
        assert new_name == 'Vancouver'
    if name == '97086':
        assert new_name == 'Happy Valley'
    if name == 'Portland, OR' or name == 'Portland, Oregon' or name == 'portland':
        assert new_name == 'Portland'
    if name == 'Beaverton, OR':
        assert new_name == 'Beaverton'
    if name == 'vernonia':
        assert new_name == 'Vernonia'


if __name__ == '__main__':

    osm_portland = 'D:/PythonProjects/UDACITY/01_Data_Analyst/03_Data_Wrangling/Data Wrangling ' \
                   'Project/portland_oregon_50_sample.osm'
    osm_portland_full = 'D:/PythonProjects/UDACITY/01_Data_Analyst/03_Data_Wrangling/Data Wrangling ' \
                        'Project/portland_oregon.osm'

    # main(osm_portland)

    test_string = ["molalla",
                   "portland",
                   "vancouver",
                   "97086",
                   "Portland, OR",
                   "Portland, Oregon",
                   "Beaverton, OR",
                   "vernonia",
                   "OR"]

    for x in test_string:
        test(x)