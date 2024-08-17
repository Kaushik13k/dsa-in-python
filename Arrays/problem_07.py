# Two sum
# https://leetcode.com/problems/two-sum/


# Bruteforce solution:
# Time Complexity: O(n^2)
# Space Complexity: O(1)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# Solution 1: using dict
# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            num_required = target - nums[i]
            if num_required in hashmap:
                return [hashmap[num_required], i]
            hashmap[nums[i]] = i


# Solution 2: using two pointers - Greedy approach
# Time complexity: O(nlogn)
# Space complexity: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted((num, i) for i, num in enumerate(nums))

        left = 0
        right = len(nums) - 1

        while left < right:
            sums = nums[left][0] + nums[right][0]
            if sums == target:
                return [nums[left][1], nums[right][1]]
            elif sums < target:
                left += 1
            else:
                right -= 1

        return []


#  (OR)
# Time complexity: O(n^2) -> Not efficient as bubble sort. the sorted() used timsort (O(nlogn) -> much efficient)
# Space complexity: O(n)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_elems = []
        for i in range(len(nums)):
            sorted_elems.append((nums[i], i))

        # Bubble Sort
        for i in range(len(sorted_elems)):
            for j in range(0, len(sorted_elems) - i - 1):
                if sorted_elems[j][0] > sorted_elems[j + 1][0]:
                    # Swap the elements
                    temp = sorted_elems[j]
                    sorted_elems[j] = sorted_elems[j + 1]
                    sorted_elems[j + 1] = temp

        left_pointer = 0
        right_pointer = len(nums) - 1
        while left_pointer < right_pointer:
            sums = sorted_elems[left_pointer][0] + sorted_elems[right_pointer][0]
            if sums == target:
                return [sorted_elems[left_pointer][1], sorted_elems[right_pointer][1]]
            elif sums < target:
                left_pointer += 1
            else:
                right_pointer -= 1
