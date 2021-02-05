class Node:
    def __init__(self, val: int):
        self.left = None
        self.right = None
        self.val = val
        self.height = 1
        self.bf = 0
class AVLTree:
    def __init__(self):
        self.root = None
        self.nodeCount = 0
    def contains(self, node, value):
        if node == None:
            return False
        cmp = self.__compare(value, node.val)
        if cmp < 0:
            return self.contains(node.left, value)
        if cmp > 0:
            return self.contains(node.right, value)
        return True
    def insert(self, value):
        if value == None:
            return False
        if self.contains(self.root, value):
            return False
        self.root = self.__insert(self.root, value)
        self.nodeCount += 1
        return True
    def __insert(self, node, value):
        if node == None:
            return Node(value)
        cmp = self.__compare(value, node.val)
        if cmp < 0:
            node.left = self.__insert(node.left, value)
        else:
            node.right = self.__insert(node.right, value)
        self.__update(node)
        return self.__balance(node)
    
    def __compare(self, val1, val2):
        return val1-val2
    def __update(self, node):
        if node.left == None:
            left_height = -1
        else:
            left_height = node.left.height
        if node.right == None:
            right_height = -1
        else:
            right_height = node.right.height
        node.height = 1 + max(left_height, right_height)
        node.bf = right_height - left_height
    def __balance(self, node):
        if node.bf == -2:
            if node.left.bf <= 0:
                return self.__left_left_case(node)
            else:
                return self.__left_right_case(node)
        elif node.bf == 2:
            if node.right.bf >= 0:
                return self.__right_right_case(node)
            else:
                return self.__right_left_case(node)
        return node
    def __right_rotate(self, node):
        temp = node.left
        node.left = temp.right
        temp.right = node
        self.__update(node)
        self.__update(temp)
        return temp
    def __left_rotate(self, node):
        temp = node.right
        node.right = temp.left
        temp.left = node
        self.__update(node)
        self.__update(temp)
        return temp
    def __left_left_case(self, node):
        return self.__right_rotate(node)
    def __right_right_case(self, node):
        return self.__left_rotate(node)
    def __left_right_case(self, node):
        node.left = self.__left_rotate(node.left)
        return self.__right_rotate(node)
    def __right_left_case(self, node):
        node.right = self.__right_rotate(node.right)
        return self.__left_rotate(node)
