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
    def pop_back(self) -> Node:
        if self.is_empty():
            raise IndexError("There is no element in the array")
        else:
            trav1 = self.head
            while trav1.next not None:
                trav2 = trav1.next
                if trav2.next == None:
                    item = trav2
                    trav1.next = None
                    self.tail = trav1
                    self._size -= 1
                    return item
                trav1 = trav2.next
            self._size -= 1
            self.head = None
            self.tail = None
            return trav1
    def pop_front(self) -> Node:
        if self.is_empty():
            raise IndexError("There is no element in the array")
        else:
            item = self.head
            self.head = item.next
            self._size -= 1
            return item
    def front(self) -> Node:
        return self.head
    def back(self) -> Node:
        return self.tail
    def insert(self, index: int, item: int) -> None:
        if self._size < index:
            raise IndexError("There is no element in the array")
        else:
            newNode = Node(item)
            curr = self.head
            if index == 0:
                self.head = newNode
                newNode.next = curr
                self._size += 1
                return 
            for i in range(1, self._size):
                if index-1 == i:
                    temp = curr.next
                    curr.next = newNode
                    newNode.next = temp
                    self._size += 1
                    return
                curr = curr.next
            temp = self.tail
            temp.next = newNode
            self.tail = newNode
            self._size += 1
            return
class Node:
    def __init__(self, val: int):
        self.next = None
        self.val = val
    def nextNode(self, next: Node):
        self.next = next

