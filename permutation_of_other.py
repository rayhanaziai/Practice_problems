"""Given a list of strings, write a method to decide if one is the permutation of the other"""


def permutation(str1, str2):
    dict_1 = {}
    dict_2 = {}
    for item in str1:
        dict_1[item] = dict_1.get(item, 0) + 1
    for item in str2:
        dict_2[item] = dict_2.get(item, 0) + 1

    for char in dict_1:
        if char not in dict_2 or dict_1[char] != dict_2[char]:
            return False

    for char in dict_2:
        if char not in dict_1 or dict_2[char] != dict_1[char]:
            return False

    return True
