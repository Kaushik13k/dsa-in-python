# Max consecutive ones
# https://leetcode.com/problems/max-consecutive-ones/description/

# Brute force solution:
# Time complexity: O(n)
# Space complexity: O(1)


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_ones = 0
        for i in nums:
            if i == 1:
                count += 1
                if max_ones < count:
                    max_ones = count
            else:
                count = 0
        return max_ones
