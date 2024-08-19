# Maximum subarray
# https://leetcode.com/problems/maximum-subarray/

# Kadane's Algorithm, maximum subarray sum
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float("-inf")
        Sum = 0
        for i in range(len(nums)):
            Sum += nums[i]

            if Sum > maxi:
                maxi = Sum

            if Sum < 0:
                Sum = 0

        return maxi
