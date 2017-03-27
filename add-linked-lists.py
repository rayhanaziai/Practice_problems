class Node(object):
    """Linked list node."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_rev_string(self):
        """Represent data for this node and its successors as a string.

        >>> l1 = Node(3)
        >>> l1.as_rev_string()
        '3'

        >>> l1 = Node(3, Node(2, Node(1)))
        >>> l1.as_rev_string()
        '123'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(reversed(out))

    def add_linked_lists(l1, l2):
        """Given two linked lists, treat like numbers and add together.

        l1: the head node of a linked list in "reverse-digit" format
        l2: the head node of another "reverse-digit" format

        Returns: head node of linked list of sum in "reverse-digit" format.
        """
        current_l1 = l1
        current_l2 = l2
        previous_node = None

        while current_l1 is not None:
            new_node = Node(current_l1.data + current_l2.data, None)
            if previous_node is not None:
                previous_node.next = new_node
            previous_node = new_node
            current_l1 = current_l1.next
            current_l2 = current_l2.next
