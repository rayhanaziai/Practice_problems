"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    p1 = head
    p2 = head.next
    while p1 is not None and p2 is not None:
        if p1 == p2:
            return True
        else:
            p2 = p2.next.next
            p1 = p1.next
    return False
