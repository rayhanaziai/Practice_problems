"""Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end of the string to hold the additional characters, and that you are given the "true" length of the string. 

eg.
input:  "Mr John Smith    "
output: "Mr%20John%20Smith"

"""

def replace_spaces(s):
    s = s.rstrip()
    my_lst = []
    for item in s:
        my_lst.append(item)

    i = 0
    while i < len(my_lst):
        if my_lst[i] == " ":
            my_lst[i] = "%20"
        i += 1
    new_str = "".join(my_lst)

    return new_str



