"""Assume you have a method is_substring which checks if one word is a substring of another. Given 2 strings, write code to check if s2 is a rotation of s1 using only one call to is_substring.

e.g "waterbottle" is a rotation of "erbottlewat"
"""


def is_substring(s1, s2):
    """returns True if s1 is a substring of s2"""

    dict_1 = {}
    dict_2 = {}

    for item in s1:
        dict_1[item] = dict_1.get(item, 0) + 1
    for item in s2:
        dict_2[item] = dict_2.get(item, 0) + 1

    for item in dict_1:
        if item not in dict_2 or dict_2[item] < dict_1[item]:
            return False

    return True


def is_rotation(s1, s2):
    """returns true if s2 is a rotation of s1"""

    if len(s2) != len(s1) or s1 is None:
        return False

    double = s1 + s1

    return is_substring(s2, double)
