class Node:
    def __init__(self, val: int):
        self.next = None
        self.val = val
    def nextNode(self, next: Node):
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
        self._size = 0
    def pop(self) -> int:
        if self._size > 0:
            item = self.head
            self.head = self.head.next
            self._size -= 1
            return item.val
        raise IndexError("There is no element in the array")
    def push(self, val: int):
        item = Node(val)
        item.next = self.head
        self.head = item
        self._size += 1
    def size(self) -> int:
        return self._size
    def is_empty(self) -> bool:
        return self._size == 0
    def peek(self) -> int:
        if self._size > 0:
            return self.head.val
        raise IndexError("There is no element in the array")


