"""Remove duplicates from an unsorted linked list.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node

"""


def remove_duplicates(head):

    seen = set()
    current = head
    previous = None
    while current is not None:
        if current.data in seen:
            current = current.next
            previous.next = current
        else:
            seen.add(current.data)
            previous = current
            current = current.next

