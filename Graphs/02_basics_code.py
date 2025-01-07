class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.weights = {}

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []
        else:
            print("Node already exists")

    def add_edge(self, u, v, weight=1):
        if u not in self.adjacency_list:
            self.add_node(u)
        if v not in self.adjacency_list:
            self.add_node(v)
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(
            u
        )  # For undirected graph; remove for directed graph
        self.weights[(u, v)] = weight
        self.weights[(v, u)] = weight
