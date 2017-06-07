class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node

    def dequeue(self):
        item = self.head
        self.head = item.next
        return item.data

    def peek(self):
        return self.head.data

    def is_empty(self):
        return not self.head