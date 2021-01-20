from practice.dataStructures.node import Node
class LinkedList:
    def __init__(self):
        self._size = 0
        self.head = None
        self.tail = None
    def size(self) -> int:
        return self._size
    def is_empty(self) -> bool:
        return self._size == 0
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
    def pop_back(self) -> int:
        if self.is_empty():
            raise IndexError("There is no element in the array")
        else:
            trav1 = self.head
            while trav1.next is not None:
                trav2 = trav1.next
                if trav2.next == None:
                    item = trav2
                    trav1.next = None
                    self.tail = trav1
                    self._size -= 1
                    return item.val
                trav1 = trav2.next
            self._size -= 1
            self.head = None
            self.tail = None
            return trav1.val
    def pop_front(self) -> int:
        if self.is_empty():
            raise IndexError("There is no element in the array")
        else:
            item = self.head
            self.head = item.next
            self._size -= 1
            if self.is_empty():
                self.tail = None
            return item.val
    def front(self) -> int:
        return self.head.val
    def back(self) -> int:
        return self.tail.val
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
    def value_at(self, index: int) -> int:
        if self._size < index:
            raise IndexError("There is no element in the array")
        else:
            curr = self.head
            for i in range(0, self._size):
                if index == i:
                    return curr.val
                curr = curr.next
            return self.tail.val
    def erase(self, index: int) -> int:
        if self._size < index:
            raise IndexError("There is no element in the array")
        else:
            curr = self.head
            if index == 0:
                self.head = curr.next
                self._size -= 1
                return curr.val
            for i in range(1, self._size):
                if index-1 == i:
                    temp = curr.next
                    curr.next = temp.next
                    self._size -= 1
                    if temp.next == None:
                        self.tail = curr
                    return temp.val
                curr = curr.next
            raise IndexError("There is no element in the array")
    def value_n_from_end(self, n: int) -> int:
        if self._size < n:
            raise IndexError("There is no element in the array")
        else:
            index = self._size - n
            curr = self.head
            for i in range(0, self._size):
                if index == i:
                    return curr.val
                curr = curr.next
            return self.tail.val
    def reverse(self):
        pre = None
        curr = self.head
        self.tail = curr
        preced = curr.next
        while preced is not None:
            curr.next = pre
            pre = curr
            curr = preced
            preced = curr.next
        curr.next = pre
        self.head = curr
    def remove_value(self, val) -> int:
        pre = None
        curr = self.head
        for _ in range(self._size):
            if val == curr.val:
                temp = curr
                pre.next = curr.next
                self._size -= 1
                return temp.val
            pre = curr
            curr = curr.next
        raise IndexError("There is no element in the array")
