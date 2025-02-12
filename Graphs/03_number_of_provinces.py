def findCircleNum(isConnected):
    def dfs(start):
        visited = []
        stack = [start]
        
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                
                for neighbor in range(len(isConnected[node])):
                    if isConnected[node][neighbor] == 1 and neighbor not in visited:
                        stack.append(neighbor)
        print(f"Returning the visited: {visited}")
        return visited

    n = len(isConnected)
    total_visited = []
    province_count = 0

    for i in range(n):
        if i not in total_visited:
            province_cities = dfs(i)
            total_visited.extend(province_cities)
            print(f"the total visited is: {total_visited}")
            province_count += 1

    return province_count


isConnected = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]
print(findCircleNum(isConnected)) 