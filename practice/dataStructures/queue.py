from practice.dataStructures.node import Node
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    def is_empty(self) -> bool:
        return self._size == 0
    def enqueue(self, value: int):
        if self.head == None:
            self.head = Node(value)
        else:
            self.tail.next = Node(value)
        self.tail = Node(value)
        self._size += 1
    def dequeue(self) -> int:
        if self.is_empty():
            raise IndexError("There is no element in the array")
        item = self.head
        self.head = self.head.next
        self._size -= 1
        if self._size == 0:
            self.tail = None
        return item.val
    def peeking(self) -> int:
        if self.is_empty():
            raise IndexError("There is no element in the array")
        return self.head.val
