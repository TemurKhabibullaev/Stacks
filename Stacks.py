from LinkedList import SinglyLinkedList


class Stacks:
    def __init__(self):
        self.ins = SinglyLinkedList()

    def push(self, data):
        self.ins.add_head(data)

    def pop(self):
        return self.ins.del_head()

    def display(self):
        return self.ins.display()

