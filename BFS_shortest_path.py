class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return (len(self.queue) == 0)

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            item = self.queue[0]
            del self.queue[0]
            return item

class Graph:
    def __init__(self, graph):
        self.g = graph
        self.n = len(self.g)

    def bfs(self, s, e):
        prev = self.solve(s)
        return self.reconstructedPath(s, e, prev)

    def solve(self, s):
        q = Queue()
        q.enqueue(s)
        visited = [False] * self.n
        visited[s] = True
        prev = [None] * self.n
        while (q.isEmpty() == False):
            node = q.dequeue()
            neighbours = self.g[node]
            for next in neighbours:
                if visited[next] == False:
                    q.enqueue(next)
                    visited[next] = True
                    prev[next] = node
        return prev

    def reconstructedPath(self, s, e, prev):
        path = []
        at = e
        while (at != None):
            path.append(at)
            at = prev[at]
        path.reverse()
        if path[0] == s:
            return path
        else:
            return []

graph = {}
graph[0] = [7, 9, 11]
graph[1] = [8, 10]
graph[2] = [3, 12]
graph[3] = [2, 4, 7]
graph[4] = [3]
graph[5] = [6]
graph[6] = [5, 7]
graph[7] = [0, 3, 6, 11]
graph[8] = [1, 9, 12]
graph[9] = [0, 8, 10]
graph[10] = [1, 9]
graph[11] = [0, 7]
graph[12] = [2, 8]

new_graph = Graph(graph)
print(new_graph.bfs(4, 10))
