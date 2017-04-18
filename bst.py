class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def is_bst(current, lowerbound=-float('inf'), upperbound=float('inf')):

    if not current:
        return True

    if (current.data < lowerbound) or (current.data > upperbound): 
        return False

    return is_bst(current.right, current.data, upperbound) and is_bst(current.left, lowerbound, current.data)


a = Node(5)
b = Node(3)
c = Node(7)
d = Node(1)
e = Node(4)
f = Node(4)
g = Node(8)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

print is_bst(a)
"""should return false"""