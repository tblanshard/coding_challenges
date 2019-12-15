class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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

class BinaryTree:
    def __init__(self):
        self.root = None
        self.numberNodes = 0

    def add(self, value):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
        else:
            self._add(self.root, newNode)

    def _add(self, node, newNode):
        queue = Queue()
        queue.enqueue(node)
        while queue.isEmpty() != True:
            item = queue.dequeue()
            print(item.value, end = " ")
            if item.left != None:
                queue.enqueue(item.left)
            else:
                item.left = newNode
                return
            if item.right != None:
                queue.enqueue(item.right)
            else:
                item.right = newNode
                return

    def quickPrint(self, node):
        if node != None:
            self.quickPrint(node.left)
            print(node.value, end=" ")
            self.quickPrint(node.right)

tree = BinaryTree()
tree.add(1)
tree.add(2)
tree.add(3)
tree.add(4)
tree.add(5)
tree.add(6)
tree.quickPrint(tree.root)
