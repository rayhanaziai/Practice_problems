class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def reverse_LL(head):
    current = head
    new_LL = None

    while current:
        new_LL = Node(current.data, new_LL)
        current = current.next

    return new_LL

a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c

print reverse_LL(a)