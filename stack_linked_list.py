class Node:
    def __init__(self, data, previous, next):
        self.data = data
        self.previous = previous
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def LL_size(self):
        return self.size

    def printLL(self):
        head = self.head
        while (head != None):
            print(head.data, end=" ")
            head = head.next

    def isEmpty(self):
        return (self.size == 0)

    def add(self, element):
        return self.addLast(element)

    def addFirst(self, element):
        if self.isEmpty():
            self.head = Node(element, None, None)
            self.tail = self.head
        else:
            self.head.previous = Node(element, None, self.head)
            self.head = self.head.previous
        self.size += 1

    def addLast(self, element):
        if self.isEmpty():
            self.tail = Node(element, None, None)
            self.head = self.tail
        else:
            self.tail.next = Node(element, self.tail, None)
            self.tail = self.tail.next
        self.size += 1

    def peekFirst(self):
        if self.isEmpty():
            return "Empty!"
        else:
            return self.head.data

    def peekLast(self):
        if self.isEmpty():
            return "Empty!"
        else:
            return self.tail.data

    def removeFirst(self):
        if self.isEmpty():
            return "Empty!"
        else:
            data = self.head.data
            self.head = self.head.next
            size -= 1
            if self.isEmpty():
                self.tail = None
            else:
                self.head.previous = None
            return data

    def removeLast(self):
        if self.isEmpty():
            return "Empty!"
        else:
            data = self.tail.data
            self.tail = self.tail.previous
            self.size -= 1
            if self.isEmpty():
                self.head = None
            else:
                self.tail.next = None
            return data

class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def push(self, element):
        self.stack.add(element)

    def pop(self):
        return self.stack.removeLast()

    def peek(self):
        return self.stack.peekLast()

    def getsize(self):
        return self.stack.LL_size()

    def printStack(self):
        self.stack.printLL()

def main():
    stack = Stack()

main()
