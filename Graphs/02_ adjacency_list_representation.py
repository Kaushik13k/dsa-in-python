class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False

    def add_edges(self, vertex1, vertex2):  # Note: This is for an undirected graph
        if (
            vertex1 in self.adjacency_list.keys()
            and vertex2 in self.adjacency_list.keys()
        ):
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            print("Edge added successfully")
            return True
        print(f"Vertex {vertex1} or {vertex2} not found")
        return False

    def remove_edges(self, vertex1, vertex2):
        if (
            vertex1 in self.adjacency_list.keys()
            and vertex2 in self.adjacency_list.keys()
        ):
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
                print("Edge removed successfully")
                return True
            except Exception as e:
                pass
        print(f"Vertex {vertex1} or {vertex2} not found")
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            print("Vertex removed successfully")
            return True
        print(f"Vertex {vertex} not found")
        return False

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(f"{vertex} : {self.adjacency_list[vertex]}")


# Working with the Graph class
print("Working with the Graph class")
graph1 = Graph()

graph1.add_vertex("A")
graph1.add_vertex("B")
graph1.add_vertex("C")
graph1.add_vertex("D")
graph1.print_graph()

graph1.add_edges("A", "B")
graph1.add_edges("A", "C")
graph1.add_edges("A", "D")
graph1.add_edges("B", "C")
graph1.add_edges("C", "D")
graph1.print_graph()

graph1.remove_edges("A", "B")
graph1.print_graph()

graph1.remove_vertex("D")
graph1.print_graph()


# Graph class with error
print("Graph class with error")
graph2 = Graph()
graph2.add_vertex("A")
# graph.add_vertex("B")
graph2.print_graph()
graph2.add_edges("A", "B")
graph2.print_graph()
