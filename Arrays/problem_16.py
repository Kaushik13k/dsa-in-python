# Rearrange array elements by sign
# https://leetcode.com/problems/rearrange-array-elements-by-sign/


# Brutforce approach:
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negatives = []
        positives = []

        for i in nums:
            if i > 0:
                positives.append(i)
            else:
                negatives.append(i)

        for i in range(len(positives)):
            nums[2 * i] = positives[i]
        for i in range(len(negatives)):
            nums[2 * i + 1] = negatives[i]
        return nums


# Optimal Approach:
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = 0
        neg = 1
        sorted_arr = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                sorted_arr[pos] = nums[i]
                pos += 2
            else:
                sorted_arr[neg] = nums[i]
                neg += 2
        return sorted_arr
