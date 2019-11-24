class Stack:
	def __init__(self):
		self.stack = []

	def push(self, data):
		self.stack.append(data)

	def pop(self):
		if (isEmpty == False):
			node = self.stack[len(self.stack) - 1]
			del node
			return node

	def isEmpty(self):
		return (len(self.stack) == 0)


class Node:
	def __init__(self, data):
		self.data = data
		self.children = []

class Tree:
    def __init__(self):
        self.root = Node("\\")
        self.count = 0

    def getRoot(self):
        return self.root

    def clearCount(self):
        self.count = 0

    def getCount(self):
        return self.count

    def addNode(self, node, data):
        for item in node.children:
            if item.data == data:
                return item
        new_node = Node(data)
        node.children.append(new_node)
        self.count += 1
        return new_node

def main():
    number_of_cases = int(input())
    for case in range(number_of_cases):
        data = input().split(" ")
        no_pre_done = int(data[0])
        no_not_done = int(data[1])
        tree = Tree()
        root = tree.getRoot()

        for done in range(no_pre_done):
            line = input().split("/")
            line = line[1:]
            node = root
            for item in line:
            	node = tree.addNode(node, item)

        tree.clearCount()

        root = tree.getRoot()
        for todo in range(no_not_done):
            line = input().split("/")
            line = line[1:]
            node = root
            for item in line:
                node = tree.addNode(node, item)
        print("Case #{}: {}".format(case + 1, tree.getCount()))

main()
