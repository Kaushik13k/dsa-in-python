class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.weights = {}

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []
        else:
            print("Node already exists")

    def add_edge(self, node, neighbor, weight=0):
        if node not in self.adjacency_list:
            self.add_node(node)
        if neighbor not in self.adjacency_list:
            self.add_node(neighbor)
        self.adjacency_list[node].append(neighbor)
        self.adjacency_list[neighbor].append(
            node
        )  # For undirected graph; remove for directed graph
        self.weights[(node, neighbor)] = weight
        self.weights[(neighbor, node)] = weight

    def print_graph(self):
        print("The graph representation is:")
        for node, neighbors in  self.adjacency_list.items():
            print(node, neighbors)
        
    def bfs(self, start):
        visited = []
        result = []
        queue = [start]

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                result.append(node)

                for neighbor in self.adjacency_list[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return result 

    def dfs(self, start):
        visited = [] 
        stack = [start]
        result = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                result.append(node)
                
                for neighbor in reversed(self.adjacency_list[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return result


graph_1 = Graph()
graph_1.add_node(node=0)
graph_1.add_node(node=1)
graph_1.add_node(node=2)
graph_1.add_node(node=3)
graph_1.add_node(node=4)
graph_1.add_node(node=5)
graph_1.add_node(node=6)

graph_1.add_edge(node=0, neighbor=1)
graph_1.add_edge(node=0, neighbor=2)
graph_1.add_edge(node=1, neighbor=3)
graph_1.add_edge(node=2, neighbor=4)
graph_1.add_edge(node=3, neighbor=5)
graph_1.add_edge(node=3, neighbor=4)
graph_1.add_edge(node=4, neighbor=5)
graph_1.add_edge(node=5, neighbor=6)

graph_1.print_graph()

print(f"The BFS representation of the graph is: {graph_1.bfs(0)}")
print(f"The DFS representation of the graph is: {graph_1.dfs(0)}")