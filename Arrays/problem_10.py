# Sort colors
# https://leetcode.com/problems/sort-colors/
# Time Complexity: O(n)
# Space Complexity: O(1)

# Brutforce solution:


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter0 = 0
        counter1 = 0
        counter2 = 0

        for i in nums:
            if i == 0:
                counter0 += 1
            elif i == 1:
                counter1 += 1
            else:
                counter2 += 1
        for i in range(counter0):
            nums[i] = 0
        for i in range(counter0, counter0 + counter1):
            nums[i] = 1
        for i in range(counter0 + counter1, counter0 + counter1 + counter2):
            nums[i] = 2
        return nums


# Optimal solution:

# Dutch national flag algorithm
# ALGO EXPLAINATION:
# [0 ... low-1] -> 0
# [low ... mid-1] -> 1
# [high+1 ... n-1] -> 2

# [0,    ...  low-1,  low, ... mid-1, mid, ...   high, high+1 ...  n-1]
#  |              |   |           |    |           |     |           |
#  v              v   v           v    v           v     v           v
# [0, 0, 0, 0, 0, 0,  1, 1, 1, 1, 1,   1, 2, 0, 1, 2,    2, 2, 2, 2, 2]

# if a[mid] == 0 -> swap(a[low], a[mid]), low++, mid++
# if a[mid] == 1 -> mid++
# if a[mid] == 2 -> swap(a[mid], a[high]), high--

# eg:
# mid
# [0, 1, 2, 0, 1, 2, 0]
# low                high


# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def swap(self, arr, a, b):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mid, low = 0, 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                self.swap(nums, low, mid)
                mid += 1
                low += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                self.swap(nums, mid, high)
                high -= 1
        return nums
