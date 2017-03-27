"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    looked_at = []
    current_node = head
    count = 0
    while current_node is not None:
        if current_node.data in looked_at:
            return True
        else:
            current_node.data = count
            count += 1
            looked_at.append(current_node.data)
            current_node = current_node.next
    return False
