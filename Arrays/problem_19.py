# Set matrix zeroes
# https://leetcode.com/problems/set-matrix-zeroes/

# Bruteforce Approach:
# Time Complexity: O(N*M*(N+M))
# Space Complexity: O(1)


class Solution:
    def markCol(self, matrix, row, col_index):
        for i in range(row):
            if matrix[i][col_index] != 0:
                matrix[i][col_index] = -1

    def markRow(self, matrix, col, row_index):
        for j in range(col):
            if matrix[row_index][j] != 0:
                matrix[row_index][j] = -1

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    self.markRow(matrix, col, i)
                    self.markCol(matrix, row, j)

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0


# Better Approach:
# Time Complexity: O(m×n)+O(m×n)=O(m×n)
# Space Complexity: O(m+n)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row = [-1] * len(matrix)
        col = [-1] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j] = 0


# Optimal Approach:
# Time Complexity: O(m×n)
# Space Complexity: O(1)


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col0 = 1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != 0:
                    if matrix[0][j] == 0 or matrix[i][0] == 0:
                        matrix[i][j] = 0
        if matrix[0][0] == 0:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if col0 == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
