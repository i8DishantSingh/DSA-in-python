class Graph:
    def __init__(self):
        self.graph = {}  # dictionary to store adjacency list

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, src, dest):
        # undirected graph: add both ways
        self.graph[src].append(dest)
        self.graph[dest].append(src)

    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

# Example usage
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "C")

g.print_graph()