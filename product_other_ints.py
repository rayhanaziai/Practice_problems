"""You have a list of integers, and for each index you want to find the product of every integer except the integer at that index. Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products."""


def get_products_of_all_ints_except_at_index(lst):
    result_lst = []
    for i in range(len(lst)):
        prod = 1
        for j in range(len(lst)):
            if i != j:
                prod = prod * lst[j]
        result_lst.append(prod)
    return result_lst

