class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Edge:
    def __init__(self, weight, src, dest):
        self.weight = weight
        self.src = src
        self.dest = dest

class Graph:
    def __init__(self, no_vertices):
        self.no_vertices = no_vertices
        self.graph = [None] * self.no_vertices
        self.edges = []

    def add_edge(self, src, dest, weight):
        edge1 = Edge(weight, src, dest)
        edge2 = Edge(weight, dest, src)
        self.edges.append(edge1)
        self.edges.append(edge2)

        dest_node = Node(dest)
        dest_node.next = self.graph[src]
        self.graph[src] = dest_node

        src_node = Node(src)
        src_node.next = self.graph[dest]
        self.graph[dest] = src_node

    def print_graph(self):
        for i in range(self.no_vertices):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            for item in self.edges:
                print(item.weight)
            while temp:
                print(" -> {}".format(temp.data), end="")
                temp = temp.next
            print("\n")

if __name__ == "__main__":
    graph = Graph(5)
    graph.add_edge(0, 1, 12)
    graph.add_edge(0, 4, 13)
    graph.add_edge(1, 2, 14)
    graph.add_edge(1, 3, 15)
    graph.add_edge(1, 4, 16)
    graph.add_edge(2, 3, 17)
    graph.add_edge(3, 4, 18)
    graph.print_graph()
