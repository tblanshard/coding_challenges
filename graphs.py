from priority_queue import PriorityQueue

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

'''
1. Add the vertex to start the breadth-first search to the empty queue. Mark that vertex visited.
2. Extract a vertex from the queue and add its neighbors to the queue if that isn't marked visited.
3. Repeat step 2 until the queue is empty.
'''

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.dfs_visited = {}
        for node in self.graph:
            self.dfs_visited[node] = False

    def bfs(self, root):
        queue = Queue()
        queue.enqueue(root)
        visited = {}
        for node in graph:
            visited[node] = False
        visited[node] = True
        while (queue.isEmpty() != True):
            removed = queue.dequeue()
            print(removed)
            for neighbour in graph[removed]:
                if (visited[removed] == False):
                    visited[removed] = True
                    queue.enqueue(neighbour)

    def dfs(self, root):
        self.dfs_visited[root] = True
        print(root)
        for neighbour in self.graph[root]:
            if (self.dfs_visited[neighbour] == False):
                self.dfs(neighbour)

if __name__ == "__main__":
    graph = {'0': ['1', '2', '3'],
         '1': ['0', '2'],
         '2': ['0', '1', '4'],
         '3': ['0'],
         '4': ['2']}
    g = Graph(graph)
    #g.bfs(0)
    g.dfs('0')
