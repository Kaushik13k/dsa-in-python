# https: // leetcode.com/problems/number-of-enclaves/

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return

        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1:
                return
            grid[r][c] = 0
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + dr, c + dc)

        for i in range(rows):
            if grid[i][0] == 1:
                dfs(i, 0)
            if grid[i][cols - 1] == 1:
                dfs(i, cols - 1)

        for j in range(cols):
            if grid[0][j] == 1:
                dfs(0, j)
            if grid[rows - 1][j] == 1:
                dfs(rows - 1, j)

        return sum(grid[i][j] for i in range(rows) for j in range(cols))
