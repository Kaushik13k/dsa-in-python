# Longest consecutive sequence
# https://leetcode.com/problems/longest-consecutive-sequence/description/

# Bruteforce Approach:
# Time Complexity: O(n^3)
# Space Complexity: O(n)


class Solution:
    def linear_search(self, ele, nums):
        for i in range(len(nums)):
            if nums[i] == ele:
                return True
        return False

    def longestConsecutive(self, nums: List[int]) -> int:
        length = 1
        for i in range(len(nums)):
            count = 1
            element = nums[i]
            while self.linear_search(element + 1, nums):
                element += 1
                count += 1
            length = max(length, count)
        return length


# Better Approach:
# Time Complexity: O(nlogn)
# Space Complexity: O(1)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        length = 1
        longest = 1
        smallest = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != smallest:
                if nums[i] == smallest + 1:
                    length += 1
                    smallest = nums[i]
                else:
                    longest = max(longest, length)
                    length = 1

        longest = max(longest, length)

        return longest


# Optimal Approach:
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sets = set()
        largest = 1

        for i in nums:
            sets.add(i)

        for i in sets:
            if i - 1 not in sets:
                count = 1
                ele = i
                while ele + 1 in sets:
                    count += 1
                    ele += 1
                largest = max(largest, count)
        return largest
