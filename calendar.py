def my_function(lst):
    lst.sort()
    result_lst = []
    i = 0
    while i < len(lst):
        lower = lst[i][0]
        upper = [lst[i][1]]
        j = i
        while j + 1 < len(lst):
            if lst[j][1] >= lst[j+1][0]:
                upper.append(max(lst[j][1], lst[j+1][1]))
                j = j + 1
            else: 
                break
        i = j + 1
        result_lst.append((lower, max(upper)))

    return result_lst

# run your function through some test cases here
# remember: debugging is half the battle!
print my_function([(1, 3), (2, 4)])