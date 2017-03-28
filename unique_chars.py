"""Implement an algorithm to determine if a string has unique characters. What if you cannot use additional data structures."""

def unique_chars(str):
    my_set = set()
    for item in str: 
        my_set.add(item)

    if len(str) == len(my_set):
        return True
    else: 
        return False
