# 1. Adjacency List

#     A
#    / \
#   B   C
#   |   |
#   D   E

# Using dictionary to represent an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

# Displaying the graph
for node, neighbours in graph.items():
    print(f"{node}: {', '.join(neighbours)}")


# 2. Adjacency Matrix

#     A
#    / \
#   B   C
#   |   |
#   D   E

#   A B C D E
# A 0 1 1 0 0
# B 1 0 0 1 0
# C 1 0 0 0 1
# D 0 1 0 0 0
# E 0 0 1 0 0


# Using a 2D list to represent an adjacency matrix
vertices = ['A', 'B', 'C', 'D', 'E']
index_map = {vertex: idx for idx, vertex in enumerate(vertices)}

adj_matrix = [[0]*len(vertices) for _ in range(len(vertices))]

edges = [
    ('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E')
]

for v1, v2 in edges:
    i, j = index_map[v1], index_map[v2]
    adj_matrix[i][j] = 1
    adj_matrix[j][i] = 1  # For undirected graph

# Displaying the adjacency matrix
print("  " + " ".join(vertices))
for i, row in enumerate(adj_matrix):
    print(vertices[i] + " " + " ".join(map(str, row)))

