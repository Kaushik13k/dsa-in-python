# Move zeroes
# https://leetcode.com/problems/move-zeroes/description/

# Time complexity: O(n)
# Space complexity: O(1)


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pt1 = 0
        for pt2 in range(len(nums)):
            if nums[pt2] != 0:
                nums[pt1], nums[pt2] = nums[pt2], nums[pt1]
                pt1 += 1
