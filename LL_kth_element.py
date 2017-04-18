"""Algorithm to find kth to last element in singly linked list"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def find_kth_from_end(head, k):
    current_n = head
    p = head
    for i in range(k):
        p = p.next
    while p is not None:
        current_n = current_n.next
        p = p.next
    return current_n

