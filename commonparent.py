class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        return self.queue

    def dequeue(self):
        if (self.isEmpty() == False):
            self.item = self.queue[0]
            self.queue = self.queue[1:]
            return self.item
        else:
            return ""

    def isEmpty(self):
        if (len(self.queue) > 0):
            return False
        else:
            return True

class Stack:
    def __init__(self):
        self.stack = []
        self.head = -1

    def push(self, item):
        self.stack.append(item)
        self.head += 1

    def pop(self):
        if self.isEmpty():
            print("Stack is empty! Cannot remove :p")
            return -1
        item = self.stack[self.head]
        del self.stack[self.head]
        self.head -= 1
        return item

    def peek(self):
        if self.isEmpty():
            print("Stack is empty! Cannot remove :p")
            return -1
        return self.stack[self.head]

    def search(self, search):
        for item in self.stack:
            if item == search:
                return True
        return False

    def isEmpty(self):
        return (len(self.stack) == 0)

    def printStack(self):
        print(self.stack)

class Tree:
    def __init__(self):
        self.root = None
        self.nodeCount = 0

    def getRoot(self):
        return self.root

    def getNodeCount(self):
        return self.nodeCount

    def add(self, value):
        if self.root == None:
            self.root = Node(value, None, None)
            self.nodeCount += 1
        else:
            self._add(self.root, value)

    def _add(self, node, value):
        if value < node.data:
            if node.left == None:
                node.left = Node(value, None, None)
                self.nodeCount += 1
            else:
                self._add(node.left, value)
        if value > node.data:
            if node.right == None:
                node.right = Node(value, None, None)
                self.nodeCount += 1
            else:
                self._add(node.right, value)

    def common_parent(self, node1, node2, compare_node):
        if ((node1 < compare_node.data and node2 > compare_node.data) or (node1 > compare_node.data and node2 < compare_node.data)):
            return compare_node.data
        else:
            if (node1 < compare_node.data):
                return self.common_parent(node1, node2, compare_node.left)
            else:
                return self.common_parent(node1, node2, compare_node.right)

    def inorder(self, node):
        if node != None:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def BFS(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.isEmpty() != True:
            item = queue.dequeue()
            print(item.data, end = " ")
            if item.left != None:
                queue.enqueue(item.left)
            if item.right != None:
                queue.enqueue(item.right)

    def DFS(self, node):
        stack = Stack()
        stack.push(node)
        while stack.isEmpty() != True:
            node = stack.pop()
            print(node.data, end = " ")
            if node.right != None:
                stack.push(node.right)
            if node.left != None:
                stack.push(node.left)

    def digLeft(self, node):
        current = node
        while current.left != None:
            current = current.left
        return current

    def remove(self, node, element):
        if node == None:
            return None
        if node.data > element:
            node.left = self.remove(node.left, element)
        elif node.data < element:
            node.right = self.remove(node.right, element)
        else:
            if node.left == None:
                rightChild = node.right
                node.data = None
                node = None
                return rightChild
            elif node.right == None:
                leftChild = node.left
                node.data = None
                node = None
                return leftChild
            else:
                temp = self.digLeft(node.right)
                node.data = temp.data
                node.right = self.remove(node.right, temp.data)
        return node







tree = Tree()
tree.add(7)
tree.add(3)
tree.add(12)
tree.add(1)
tree.add(2)
tree.add(4)
tree.add(9)
tree.add(8)
tree.add(17)
tree.add(11)
tree.add(10)
root = tree.getRoot()
tree.inorder(root)
print()
print(tree.remove(root, 9))
tree.inorder(root)
print()
print(tree.common_parent(8, 11, root))
tree.BFS(root)
print()
tree.DFS(root)
