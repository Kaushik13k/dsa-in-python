# Majority element
# https://leetcode.com/problems/majority-element/


# Brutforce solution:
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        majority = len(nums) // 2

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        for key, value in hashmap.items():
            if value > majority:
                return key


# Optimal solution
# Time Complexity: O(n)
# Space Complexity: O(1)
# Boyer-Moore Voting Algorithm: increase if simmilar, decrease if not. if count == 0 assign element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        element = 0
        for i in nums:
            if count == 0:
                count += 1
                element = i
            else:
                if i == element:
                    count += 1
                else:
                    count -= 1
        return element
