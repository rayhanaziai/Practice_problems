class Node(object):
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BST(object):
    def __init__(self):
        self.root = None

    def insert_n(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
        else:
            if new_node.data > self.root.data:
                if new_node.right is not None:
                    self.insert_n(self.root.right)
                else:
                    new_node.right = new_node
            elif new_node.data < self.root.data:
                if new_node.left is not None:
                    self.insert_n(self.root.left)
                else:
                    new_node.left = new_node


