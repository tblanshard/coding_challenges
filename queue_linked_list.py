from stack_linked_list import LinkedList

class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, item):
        self.queue.addLast(item)

    def dequeue(self):
        self.queue.removeFirst()

    def printQueue(self):
        print(self.queue.printLL())

def main():
    queue = Queue()
    queue.printQueue()
    queue.enqueue(5)
    queue.printQueue()
    queue.enqueue(7)
    queue.printQueue()
    queue.enqueue(8)
    queue.printQueue()
    queue.dequeue()
    queue.printQueue()

main()
