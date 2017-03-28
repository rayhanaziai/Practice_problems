"""Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?"""


input = [["a", "b", "c", "d"], 
        ["e", "f", "g", "h"], 
        ["i", "j", "k", "l"], 
        ["m", "n", "o", "p"]]

output = [["m", "i", "e", "a"], 
        ["n", "j", "f", "b"], 
        ["o", "k", "g", "c"], 
        ["p", "l", "h", "d"]]

def rotate_matrix(input_lst):
    output_lst = zip(*input_lst[::-1])

    return output_lst


print rotate_matrix(input)



