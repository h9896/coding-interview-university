class Node:
    def __init__(self, val: int):
        self.next = None
        self.val = val
    def nextNode(self, next: Node):
        self.next = next