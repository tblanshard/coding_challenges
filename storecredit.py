class Node:
	def __init__(self, data):
		self.value = data
		self.left = None
		self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, value):
        if (self.root == None):
            self.root = Node(value)
        else:
            self._add(value, self.root)

    def _add(self, value, node):
        if (value < node.value):
            left = node.left
            if (left == None):
                node.left = Node(value)
            else:
                self._add(value, left)
        else:
            right = node.right
            if (right == None):
                node.right = Node(value)
            else:
                self._add(value, right)

    def inorder(self, node, arr):
        if (node != None):
            self.inorder(node.left, arr)
            arr.append(node.value)
            #print(node.value, end = " ")
            self.inorder(node.right, arr)
        return arr

def main():
    outputs = {}
    number_of_cases = int(input())
    for case in range(number_of_cases):
        credit = int(input())
        number_of_items = int(input())
        inputs = list(map(int, (input().split(" "))))
        items = Tree()
        for item in inputs:
            items.add(item)
        orderedItems = []
        orderedItems = items.inorder(items.getRoot(), orderedItems)
        for i, item in enumerate(orderedItems):
            for j, item2 in enumerate(orderedItems):
                #print("possible combo: {}, {}".format(item, item2))
                if ((item + item2 == credit) and (i != j)):
                    if (case + 1) not in outputs:
                        index1 = inputs.index(item) + 1
                        index2 = inputs.index(item2) + 1
                        if index1 > index2:
                            outputs[case + 1] = [index2, index1]
                        elif (index1 == index2):
                            outputs[case + 1] = [i + 1, j + 1]
                        else:
                            outputs[case + 1] = [index1, index2]
    #print(outputs)
    for item in outputs:
        print("Case #{}: {} {}".format(item, outputs[item][0], outputs[item][1]))

main()
