"""here is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.

The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.

If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

eg.
Input: [[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]]
Output: 2"""


def least_bricks(input_lst):
    wall_height = len(input_lst)
    my_dict = {}
    for line in input_lst:
        i = 0
        for item in line[:-1]:
            i += item
            my_dict[i] = my_dict.get(i, 0) + 1
    least_number = wall_height - max(my_dict.values()+[0])
    return least_number


print least_bricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]])
