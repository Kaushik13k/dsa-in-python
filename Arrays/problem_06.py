# Max consecutive ones
# https://leetcode.com/problems/max-consecutive-ones/description/


# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
                if count > maxi:
                    maxi = count
            else:
                count = 0
        return maxi
