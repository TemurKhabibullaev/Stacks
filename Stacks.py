

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stacks:
    def __init__(self):
        self.head = None
# Add head

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
# Delete head

    def pop(self):
        ret = self.head.data
        self.head = self.head.next
        return ret

    def display(self):
        elems = []
        current = self.head
        elems.append(current.data)
        while current.next:
            current = current.next
            elems.append(current.data)
        return elems

