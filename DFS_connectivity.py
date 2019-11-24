class DFS:
    def __init__(self, graph):
        self.graph = graph
        self.n = len(self.graph)
        self.count = 0
        self.components = [0] * self.n
        self.visited = [False] * self.n

    def findComponents(self):
        for i in range(self.n):
            if (self.visited[i] == False):
                self.count += 1
                self.dfs(i)
        return (self.count, self.components)

    def dfs(self, at):
        self.visited[at] = True
        self.components[at] = self.count
        for next in self.graph[at]:
            if self.visited[next] == False:
                self.dfs(next)

graph = {}
graph[0] = [8]
graph[1] = [5]
graph[2] = [9, 15]
graph[3] = [9]
graph[4] = [0]
graph[5] = [16, 17]
graph[6] = [7, 11]
graph[7] = [6, 11]
graph[8] = [4, 14]
graph[9] = [2, 3, 15]
graph[10] = [15]
graph[11] = [6, 7]
graph[12] = []
graph[13] = [0]
graph[14] = [0, 13]
graph[15] = [2, 9, 10]
graph[16] = []
graph[17] = []

dfs = DFS(graph)
dfs.count, dfs.components = dfs.findComponents()
print(dfs.count)
