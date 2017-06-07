def reverse_list(l, first_letter, last_letter):
    i = first_letter
    j = last_letter
    while i < j:
        l[i], l[j] = l[j], l[i]
        i += 1
        j -= 1
    return l


def reverse_s(s):
    char_lst = list(s)
    reverse_list(char_lst, 0, len(char_lst)-1)

    i = 0
    for end_letter in xrange(len(char_lst)):
        if (char_lst[end_letter] == " "):
            reverse_list(char_lst, i, end_letter-1)
            i = (end_letter + 1)
        elif (end_letter == len(char_lst)-1):
            reverse_list(char_lst, i, end_letter)
    return ''.join(char_lst)


# run your function through some test cases here
# remember: debugging is half the battle!
print reverse_s('hi my name is ray')