# def in_list(number, lst):
#     if not lst:
#         return False
#     if len(lst) == 1:
#         if lst[0] == number:
#             return True
#         else:
#             return False

#     mid_point = len(lst)/2
#     return in_list(number, lst[:mid_point]) or in_list(number, lst[mid_point:])
        
# lst = [1,3,4,6,7,9]

# print in_list(5, lst)

def in_list(number, lst):
    if not lst:
        return False
    if len(lst) == 1:
        if lst[0] == number:
            return True
        else:
            return False

    mid_point = lst[len(lst)/2]
    if mid_point == number: 
        return True
    elif mid_point > number: 
        return in_list(number, lst[:len(lst)/2])
    else: 
        return in_list(number, lst[len(lst)/2:])

lst = [1,3,4,6,7,9]

print in_list(6, lst)