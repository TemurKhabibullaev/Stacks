from LinkedList import SinglyLinkedList

ins = SinglyLinkedList()


class Stacks:
    def push(self, data):
        ins.add_head(data)

    def pop(self):
        return ins.del_head()

    def display(self):
        return ins.display()

