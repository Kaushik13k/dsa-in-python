# Linear Search
# https://www.geeksforgeeks.org/problems/who-will-win-1587115621/1


# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    ##Complete this function
    def searchInSorted(self, arr, N, K):
        for i in range(0, N):
            if arr[i] == K:
                return 1
        return -1
