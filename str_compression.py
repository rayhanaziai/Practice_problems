"""Implement a method to perform basic string compression using the counts of repeated characters. e.g. the stinrg aabcccccaaa would become a2b1c5a3. If the "compresed" string would not become smaller than the original string, your method should return the original string"""

def str_compression(s):
    result_lst = []
    i = 0
    while i < len(s):
        current_letter = s[i]
        count = 1
        j = i + 1
        while j < len(s):
            if s[j] == current_letter:
                count += 1
                j += 1
            else: 
                break
        result_lst.append(current_letter+str(count))
        i = i + count

    result_str = "".join(result_lst)

    if len(result_str) > len(s):
        return s
    else: 
        return result_str

