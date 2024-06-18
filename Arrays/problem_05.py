# Missing Number
# https://leetcode.com/problems/missing-number/


# Time complexity: O(n)
# Space complexity: O(1)


# Solution 1: Sum method
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        total = 0
        for i in nums:
            total += i
        return expected_sum - total


# Solution 1: XOR method
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor_all = 0

        for i in range(n):
            xor_all ^= i ^ nums[i]
        xor_all ^= n
        return xor_all
