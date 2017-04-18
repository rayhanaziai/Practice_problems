"""Reverse the words in a string in place.

eg. 'Hello I am Ray' becomes 'Ray am I Hello'"""


def word_reversal(str):
    my_lst = str.split(" ")
    for i in range(len(my_lst)/2):
        my_lst[i], my_lst[-1-i] = my_lst[-1-i], my_lst[i]
    return " ".join(my_lst)

print word_reversal("Hello I am Ray's friend")