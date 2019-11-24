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

dec = int(input())
stack = Stack()
bin = ""

while dec != 0:
    stack.push(dec % 2)
    dec = dec // 2

while (stack.isEmpty() != True):
    bin += str(stack.pop())

print(bin)
