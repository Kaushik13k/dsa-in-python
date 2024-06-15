# Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        pt1 = 0
        for pt2 in range(1, len(nums)):
            if nums[pt2] != nums[pt1]:
                pt1 += 1
                nums[pt1] = nums[pt2]
        return pt1 + 1
