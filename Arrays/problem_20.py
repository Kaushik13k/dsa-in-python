# Rotate image
# https://leetcode.com/problems/rotate-image/


# Optimal Approach:
# Time Complexity: O(n^2)
# Space Complexity: O(1)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # Transpose
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reversing
        for i in range(n):
            matrix[i].reverse()
