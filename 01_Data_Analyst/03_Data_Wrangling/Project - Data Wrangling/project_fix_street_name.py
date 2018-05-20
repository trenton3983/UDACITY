"""
Fixes street names according to the mapping structure.
Single letter cardinal directions were not corrected to long form (e.g.
N. N St => North North Street instead of North N Street)
"""

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


def fix_street_name(name, mapping=MAPPING):
    """
    Splits tag.attrib['v'] and checks each string against MAPPING.
    If there's a value match, the string is changed to the new value.
    Args:
        name (str): "NW 23rd Ave"
        mapping (dict): "Ave": "Avenue"
    Returns:
        name (str): 'Northwest 23rd Avenue
    """
    name = name.strip()
    x = name.split()
    for y in x:
        if y in mapping:
            name = name.replace(y, mapping[y])
    return name


if __name__ == '__main__':

    test_string = ['SW Evan Ct.',
                   'Powell Blvd',
                   'Dawkins Rd.',
                   'Senior Dr',
                   'S Poopy Pants Ln TRL',
                   'N. N St']

    for street in test_string:
        print(fix_street_name(street))