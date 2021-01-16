class LinkedList:
    def __init__(self):
        self._size = 0
        self.head = None
        self.tail = None
    def size(self) -> int:
        return self.size
    def is_empty(self) -> bool:
        return self.size == 0
    def push_back(self, item: int) -> None:
        if self.head == None:
            self.head = Node(item)
        else:
            self.tail.next = Node(item)
        self.tail = Node(item)
        self._size += 1
    def push_front(self, item: int) -> None:
        if self.is_empty():
            self.head = Node(item)
            self.tail = Node(item)
        else:
            new_node = Node(item)
            new_node.next = self.head
            self.head = new_node
        self._size += 1

class Node:
    def __init__(self, val: int):
        self.next = None
        self.val = val
    def nextNode(self, next: Node):
        self.next = next

