class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, item, priority):
        if len(self.queue) == 0:
            self.queue.append((item, priority))
            return self.queue
        else:
            for i, value in enumerate(self.queue):
                if value[1] > priority:
                    self.queue = self.queue[:i] + [(item, priority)] + self.queue[i:]
                    return self.queue
            self.queue.append((item, priority))

    def printqueue(self):
        print(self.queue)

    def getHighestPriority(self):
        return self.queue[0]

    def deleteHighestPriority(self):
        self.queue = self.queue[1:]
        return self.queue

queue = PriorityQueue()
queue.insert("fish", 2)
queue.insert("dog", 1)
queue.insert("cat", 3)
queue.insert("human", 2)
queue.printqueue()
print(queue.getHighestPriority())
queue.deleteHighestPriority()
queue.printqueue()
#dog, fish, human, cat
