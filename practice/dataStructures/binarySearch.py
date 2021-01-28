from practice.dataStructures.treeNode import TreeNode
class BinarySearch:
    def __init__(self):
        self.root = None
        self._size = 0
    def recurse_insert(self, current_node: TreeNode, val: int):
        if (current_node.val >= val):
            if (current_node.left is not None):
                self.recurse_insert(current_node.left, val)
            else:
                current_node.left = TreeNode(val)
        else:
            if (current_node.right is not None):
                self.recurse_insert(current_node.right, val)
            else:
                current_node.right = TreeNode(val)
    def recurse_find(self, current_node: TreeNode, val: int) -> TreeNode:
        if (current_node.val == val):
            return current_node
        elif (current_node.val > val):
            if (current_node.left is not None):
                return self.recurse_find(current_node.left, val)
            else:
                raise ValueError("The value %s doesn't exist" %val)
        else:
            if (current_node.right is not None):
                return self.recurse_find(current_node.right, val)
            else:
                raise ValueError("The value %s doesn't exist" %val)
    def recurse_remove(self, current_node: TreeNode, val: int) -> TreeNode:
        if (current_node.val > val):
            current_node.left = self.recurse_remove(current_node.left, val)
        elif (current_node.val < val):
            current_node.right = self.recurse_remove(current_node.right, val)
        else:
            if current_node.left is None:
                righ_part = current_node.right
                current_node.val = None
                current_node = None
                return righ_part
            elif current_node.right is None:
                left_part = current_node.left
                current_node.val = None
                current_node = None
                return left_part
            else:
                temp_node = current_node.right
                while temp_node.left is not None:
                    temp_node = temp_node.left
                current_node.val = temp_node.val
                current_node.right = self.recurse_remove(current_node.right, temp_node.val)
        return current_node
    def recurse_height(self, node: TreeNode):
        if node == None:
            return 0
        return max(self.recurse_height(node.left), self.recurse_height(node.right)) + 1
    def preorder(self, node: TreeNode):
        if node == None:
            return
        print(node.val)
        self.preorder(node.left)
        self.preorder(node.right)
    def inorder(self, node: TreeNode):
        if node == None:
            return
        self.preorder(node.left)
        print(node.val)
        self.preorder(node.right)
    def postorder(self, node: TreeNode):
        if node == None:
            return
        self.preorder(node.left)
        self.preorder(node.right)
        print(node.val)
    def levelorder(self):
        arr = []
        if self.is_empty():
            return
        arr.append(self.root)
        while len(arr) != 0:
            temp = arr.pop(0)
            print(temp.val)
            if (temp.right is not None):
                arr.append(temp.right)
            if (temp.left is not None):
                arr.append(temp.left)
    def size(self) -> int:
        return self._size
    def is_empty(self) -> bool:
        return self._size == 0
    def insert(self, val: int):
        if self.root == None:
            self.root = TreeNode(val)
        else:
            self.recurse_insert(self.root, val)
        self._size += 1
    def find(self, val: int) -> TreeNode:
        if self.root == None:
            raise ValueError("The value %s doesn't exist" %val)
        else:
            return self.recurse_find(self.root, val)
    def remove(self, val: int) -> bool:
        if(self.find(val) is not None):
            self.recurse_remove(self.root, val)
            self._size -= 1
            return True
        return False
    def heigh(self) -> int:
        return self.recurse_height(self.root)
    def travesal(self, travesal_type: str):
        if travesal_type.upper() == "PREORDER":
            self.preorder(self.root)
        elif travesal_type.upper() == "INORDER":
            self.inorder(self.root)
        elif travesal_type.upper() == "POSTORDER":
            self.postorder(self.root)
        elif travesal_type.upper() == "LEVELORDER":
            self.levelorder()
        else:
            raise ValueError("The travesal_type %s doesn't support" %travesal_type)
