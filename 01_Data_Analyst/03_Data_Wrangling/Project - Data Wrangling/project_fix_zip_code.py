"""Changes zip codes into a standard 5 digit US zip code"""

import re


def fix_zip_codes(zip_codes):
    """
    Expects a string.  Will search the string for a consecutive 5 digits and
    return the string as a zip code or leave blank if there's no match.
    :param zip_codes:
        (str) 'Portland OR 972233409'
    :return:
        (str) '97223'
    """

    zip_code = re.compile('\d{5}')
    zip_code = zip_code.findall(zip_codes)

    if zip_code:
        return zip_code[0]
    else:
        return ''


def test(name):

    new_name = fix_zip_codes(name)
    print(name, "=>", new_name)

    if name == 'Portland OR 972233409':
        assert new_name == '97223'
    if name == 'OR':
        assert new_name == ''
    if name == '97223':
        assert new_name == '97223'
    if name == '97223-3409':
        assert new_name == '97223'
    if name == '972233409':
        assert new_name == '97223'


if __name__ == '__main__':

    test_string = ['Portland OR 972233409',
                   'OR',
                   '97223',
                   '97223-3409',
                   '972233409']

    for x in test_string:
        test(x)



