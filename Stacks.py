

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stacks:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

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
        print(elems)

stack_instance = Stacks
stack_instance.push(4)