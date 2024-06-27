# Number of provinces
# https://leetcode.com/problems/number-of-provinces/description/

# Time complexity: O(n^2)
# Space complexity: O(n)


class Solution:
    def dfs(self, i, isConnected, visited):
        for j in range(len(isConnected)):
            if isConnected[i][j] == 1 and not visited[j]:
                visited[j] = True
                self.dfs(j, isConnected, visited)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * len(isConnected)
        provinces = 0
        for i in range(len(isConnected)):
            if not visited[i]:
                self.dfs(i, isConnected, visited)
                provinces += 1
        return provinces
