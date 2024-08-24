# Pascal Triangle
# Problem Type-1
# tell the number at ith row and jth column of pascal triangle


def pascal_triangle(n, k):
    if k == 0 or k == n:
        return 1
    res = 1
    for i in range(1, k + 1):
        res = res * (n - i)
        res = res // i + 1
    return res


# Problem Type-3
# https://leetcode.com/problems/pascals-triangle/
# Brutforce Approach:
# Time Complexity: O(n^3)
# Space Complexity: O(1)


class Solution:
    def ncr(self, n, r):
        if r > n:
            return 0
        if r == 0 or r == n:
            return 1
        if r > n - r:
            r = n - r
        res = 1
        for i in range(r):
            res = res * (n - i) // (i + 1)
        return res

    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for row in range(numRows):
            templst = []
            for i in range(row + 1):
                templst.append(self.ncr(row, i))
            ans.append(templst)
        return ans


# Optimal Approach:
# Time Complexity: O(n^2)
# Space Complexity: O(1)

from typing import *


def generateRow(row):
    ans = 1
    ansRow = [1]

    for col in range(1, row):
        ans *= row - col
        ans //= col
        ansRow.append(ans)
    return ansRow


def pascalTriangle(n: int) -> List[List[int]]:
    ans = []

    for row in range(1, n + 1):
        ans.append(generateRow(row))
    return ans
