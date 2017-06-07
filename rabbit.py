def rabbit(matrix):
    if len(matrix[0]) % 2 != 0:
        i = [len(matrix[0])/2]
    else:
        i = [len(matrix[0])/2 - 1, len(matrix[0])/2]    
    if len(matrix) % 2 != 0:
        j = [len(matrix)/2]
    else:
        j = [len(matrix)/2 - 1, len(matrix)/2]
    print i, j

    largest_value = {}
    for a in i:
        for b in j:
            largest_value[matrix[b][a]] = (a, b)
    print largest_value
    max_carrot = largest_value[max(largest_value)]
    print 'max_carrot=', max_carrot
 
        
matrix = [[1,2,3,4],
          [1,2,3,4],
          [1,2,3,4],
          [1,2,3,4]]

# matrix = [[1,2,3,4,5],
#           [1,2,3,4,5],
#           [1,2,3,4,5],
#           [1,2,3,4,5],
#           [1,2,3,4,5]]

# matrix = [[1,2,3,4],
#           [1,2,3,4],
#           [1,2,3,4],
#           [1,2,3,4],
#           [1,2,3,4]]

# matrix = [[1,2,3],
#           [1,2,3],
#           [1,2,3],
#           [1,2,3]]
