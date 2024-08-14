# Single number
# https://leetcode.com/problems/single-number/


# Bruteforce solution:


# Approach 1: Using hashing(list)
# Time Complexity: O(n+m)
# Space Complexity: O(m)
# Drawback: It is not optimal as it uses extra space
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        biggest_number = max(nums)
        hashlist = [0] * (biggest_number + 1)
        for i in nums:
            hashlist[i] += 1

        for count in range(len(hashlist)):
            if hashlist[count] == 1:
                return count


# Approach 2: Using hashmap
# Time complexity: O(2n)
# Space complexity: O(n)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        for value, count in hashmap.items():
            if count == 1:
                return value


# Optimal solution:
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for i in nums:
            xor ^= i
        return xor
