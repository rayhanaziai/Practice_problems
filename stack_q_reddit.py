class Node(object):
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous


class Stack(object):
    def __init__(self, max):
        self.head = None
        self.tail = None
        self.max = max
        self.length = 0
        self.set = set()

    def add_item(self, data):
        new_item = Node(data)

        if self.head is None:
            if self.max == 0:
                self.head = new_item
                self.tail = new_item
                self.length += 1
                self.set.add(new_item)
            else:
                return "not possible"

        else:
            if self.max == self.length:
                oldest = self.head
                self.set.remove(oldest)
                self.head = self.head.next
            current_tail = self.tail
            self.tail.next = new_item
            new_item.previous = current_tail
            self.tail = new_item
            self.set.add(new_item)


