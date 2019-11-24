class Node:
    def __init__(self, value):
        self.bf = 0
        self.value = value
        self.height = 0
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.nodeCount = 0
        self.root = None

    def height(self):
        if self.root == None:
            return 0
        else:
            return root.height

    def size(self):
        return self.nodeCount

    def contains(node, value):
        if node == None:
            return False
        if value < node.value:
            return self.contains(node.left, value)
        if vale > node.value:
            return self.contains(node.right, value)
        return True

    def insert(value):
        if value == None:
            return False
        if (self.contains(self.root, value) == False):
            self.root = self._insert(self.root, value)
            self.nodeCount += 1
            return True
        return False

    def _insert(node, value):
        if node == Null:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
        self.update(node)
        return self.balance(node)

    def update(node):
        if node.left == None:
            leftNodeHeight = -1
        else:
            leftNodeHeight = node.left.height
        if node.right == None:
            rightNodeHeight = -1
        else:
            rightNodeHeight = node.right.height
        node.height = 1 + max(leftNodeHeight, rightNodeHeight)
        node.bf = rightNodeHeight - leftNodeHeight

    def balance(node):
        if (node.bf == -2):
            if node.left.bf <= 0:
                return self.leftLeftCase(node)
            else:
                return self.leftRightCase(node)
        elif (node.bf == 2):
            if node.left.bf >= 0:
                return self.rightRightCase(node)
            else:
                return self.rightLeftCase(node)
        return node

    def leftLeftCase(node):
        return self.rightRotation(node)

    def leftRightCase(node):
        node.left = self.leftRotation(node.left)
        return self.leftLeftCase(node)

    def rightRightCase(node):
        return self.leftRotation(node)

    def rightLeftCase(node):
        node.right = self.rightRotation(node.right)
        return self.rightRightCase(node)

    def leftRotation(node):
        newParent = node.right
        node.right = newParent.left
        newParent.left = node
        update(node)
        update(newParent)
        return newParent

    def rightRotation(node):
        newParent = node.left
        node.left = newParent.right
        newParent.right = node
        update(node)
        update(newParent)
        return newParent

    def remove(elem):
        if elem == None:
            return False
        if contains(self.root, elem):
            self.root = self._remove(self.root, elem)
            nodeCount -= 1
            return True
        return False

    def _remove(node, elem):
        if node == None:
            return None
        if elem < node.value:
            node.left = self._remove(node.left, elem)
        elif elem > node.value:
            node.right = self._remove(node.right, elem)
        else:
            if node.left == None:
                return node.right
            elif node.right == None:
                return node.left
            else:
                if (node.left.height > node.right.height):
                    successorValue = self.findMax(node.left)
                    node.value = successorValue
                    node.left = self._remove(node.left, successorValue)
                else:
                    successorValue = self.findMin(node.right)
                    node.value = successorValue
                    node.right = self._remove(node.right, successorValue)
        self.update(node)
        return self.balance(node)

    def findMin(node):
        while (node.left != None):
            node = node.left
        return node.value

    def findMax(node):
        while (node.right != None):
            node = node.right
        return node.value
