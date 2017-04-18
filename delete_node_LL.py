"""Delete a node from a linked list, given the node to delete """


class Node(object):
    def __init__(self, data=None, next_n=None):
        self.data = data
        self.next = next_n


def delete_n(node):
    next_n = node.next
    node.data = next_n.data
    node.next = next_n.next

"""Note that this problem cannot be solved if the node to be deleted is the last node in the LL. That's okay - point thsi out to your interviewer. Can handle this by marking the node as a dummy."""