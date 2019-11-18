class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def inorder(self, root):
        if root != None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root != None:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root != None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")


tree = Node(1, Node(12, Node(5, None, None), Node(6, None, None)), Node(9, None, None))

tree.inorder(tree)
print("\n")
tree.preorder(tree)
print("\n")
tree.postorder(tree)
