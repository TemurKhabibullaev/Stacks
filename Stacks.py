from LinkedList import SinglyLinkedList
instance = SinglyLinkedList()


class Stacks:
    def __init__(self):
        self.head = instance.head()

    def push(self, data):
        instance.add_head(data)

    def pop(self):
        instance.del_head()
