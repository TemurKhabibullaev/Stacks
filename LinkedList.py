class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def head(self):
        if self.head is not None:
            return self.head.data
        else:
            return "Empty List"

    def add_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def del_head(self):
        print(self.head.data)
        self.head = self.head.next

    def display(self):
        elems = []
        current = self.head
        elems.append(current.data)
        while current.next:
            current = current.next
            elems.append(current.data)
        print(elems)