"""Given a list of integers, find the highest product you can get from three of the integers. The input list_of_ints will always have at least three integers."""

def highest_prod(lst):
    # write the body of your function here
    prod = 1
    maxi = max(lst)
    count = 0
    while count != 3:
        for i in range(len(lst)):
            if lst[i] == maxi:
                prod = prod * lst.pop(i)
                maxi = max(lst)
                count += 1
    return prod