# input: 2 strings
# output: a single integer denoting the number of characters you must delete to make the two strings anagrams of each other


def number_needed(a, b):
    deletions = 0

    dict_a = {}
    for item in a:
        dict_a[item] = dict_a.get(item, 0) + 1

    dict_b = {}
    for item in b:
        dict_b[item] = dict_b.get(item, 0) + 1

    for item in dict_a:
        if dict_b.get(item):
            if dict_b[item] == dict_a[item]:
                continue
            elif dict_b[item] > dict_a[item]:
                deletions += (dict_b[item]-dict_a[item])
                dict_b[item] = dict_a[item]
            elif dict_a[item] > dict_b[item]:
                deletions += (dict_a[item]-dict_b[item])
                dict_a[item] = dict_b[item]
        else:
            deletions += dict_a[item]
            dict_a[item] = 0

    b_sum = 0
    b_values = dict_b.values()
    for val in b_values:
        b_sum += val

    a_sum = 0
    a_values = dict_a.values()
    for val in a_values:
        a_sum += val

    if b_sum > a_sum:
        remainder = b_sum - a_sum
    else:
        remainder = 0

    deletions += remainder
    return (deletions)

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
