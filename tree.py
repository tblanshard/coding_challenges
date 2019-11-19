class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

class BTree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, value):
        if self.root == None:
            self.root = Node(value, None, None)
        else:
            self._add(self.root, value)

    def _add(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = Node(value, None, None)
            else:
                self._add(node.left, value)
        if value > node.value:
            if node.right == None:
                node.right = Node(value, None, None)
            else:
                self._add(node.right, value)

    def find(self, value):
        if self.root.value == value:
            return True
        else:
            value = (self._find(self.root, value))
            return value

    def _find(self, node, value):
        if value < node.value:
            if node.left == None:
                print("a")
                return False
            elif node.left.value == value:
                print("b")
                return True
            else:
                print("c")
                self._find(node.left, value)
        if value > node.value:
            if node.right == None:
                print("d")
                return False
            elif node.right.value == value:
                print("e")
                return True
            else:
                print("f")
                self._find(node.right, value)

    def inorder(self, node):
        if node != None:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node != None:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node != None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")

tree2 = Node(1, Node(12, Node(5, None, None), Node(6, None, None)), Node(9, None, None))
tree1 = BTree()

tree1.add(1)
tree1.add(12)
tree1.add(5)
tree1.add(6)
tree1.add(9)

tree1.inorder(tree1.getRoot())
print("\n")
tree1.preorder(tree1.getRoot())
print("\n")
tree1.postorder(tree1.getRoot())
print("\n")
print(tree1.find(5))
print(tree1.find(22))
