"""Write code to partition a LL around a value x, such that all nodes less than x come before all nodes greater than or equal to x"""

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def partition(head, x):
    LL_1 = []
    LL_2 = []
    LL_equal = []
    current_node = head
    while current_node is not None:
        if current_node.data < x:
            LL_1.append(current_node)
        elif current_node.data > x:
            LL_2.append(current_node)
        else:
            LL_equal.append(current_node)
        current_node = current_node.next

    i = 0
    while i < len(LL_1) - 1:
        LL_1[i].next = LL_1[i+1]

    i = 0
    while i < len(LL_2) - 1:
        LL_2[i].next = LL_2[i+1]

    i = 0
    while i < len(LL_equal) - 1:
        LL_equal[i].next = LL_equal[i+1]

    LL_1[-1].next = LL_equal[0]
    LL_equal[-1].next = LL_2[0]

    return LL_1[0]
