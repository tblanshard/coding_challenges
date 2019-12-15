class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None
        self.weight = None


# A class to represent a graph. A graph
# is the list of the adjacency lists.
# Size of the array will be the no. of the
# vertices "V"
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[None, {}]] * self.V
        print(self.graph)

    # Function to add an edge in an undirected graph
    def add_edge(self, src, dest, weight):
        # Adding the node to the source node
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src][0] = node
        self.graph[src][1][node.vertex] = weight

        # Adding the source node to the destination as
        # it is the undirected graph
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest][0] = node
        self.graph[dest][1][node.vertex] = weight
        print(self.graph[dest][1])
        print(self.graph)

    # Function to print the graph
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head ".format(i), end="")
            temp = self.graph[i]
            print(temp[1])
            #while temp:
                #print(" -({})> {}".format(temp[1][temp[0].vertex],temp[0].vertex), end="")
                #temp = temp[0].next
            print(" \n")

if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1, 5)
    graph.add_edge(0, 4, 2)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 2)
    graph.add_edge(1, 4, 4)
    graph.add_edge(2, 3, 2)
    graph.add_edge(3, 4, 6)

    graph.print_graph()
