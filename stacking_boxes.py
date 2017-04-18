"""stacking boxes code"""
from itertools import permutations
from operator import itemgetter


def max_height(b1, b2, b3):
    """Each b is an array with length, width, height in an array"""

    for i, item in b1:
        b1[i] = str(item)
    for i, item in b2:
        b2[i] = str(item)
    for i, item in b3:
        b3[i] = str(item)

    b1_str = "".join(b1)
    b2_str = "".join(b2)
    b3_str = "".join(b3)

    list_of_perms = []

    for i in permutations[b1_str]:
        list_of_perms.append(int(i))
    for i in permutations[b2_str]:
        list_of_perms.append(int(i))
    for i in permutations[b3_str]:
        list_of_perms.append(int(i))

    for i in list_of_perms: 
        base_area = i[0]*i[1]
        i.append(base_area)

    list_of_perms = sorted(list_of_perms, key=itemgetter(3))
    list_of_perms.reverse()

    print list_of_perms

