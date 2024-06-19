# Two sum
# https://leetcode.com/problems/two-sum/


# Solution 1: using dict
# Time complexity: O(n)
# Space complexity: O(n)
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in index_map:
                return [index_map[complement], i]
            index_map[num] = i
        return []


# Solution 2: using two pointers
# Time complexity: O(n) + O(n logn)
# Space complexity: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted((num, i) for i, num in enumerate(nums))

        left = 0
        right = len(nums) - 1

        while left < right:
            sums = nums[left][0] + nums[right][0]
            if sums == target:
                return [nums[left][1], nums[right][1]]
            elif sums < target:
                left += 1
            else:
                right -= 1

        return []
