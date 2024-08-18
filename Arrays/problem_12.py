# Longest sub-array with sum


# Brute Force Approach:
# Time Complexity: ~ O(n^3)
# Space Complexity: O(1)


# Solution-1:
class Solution:
    def lenOfLongSubarr(self, arr, n, k):
        # Complete the function
        length = 0
        for i in range(n):
            for j in range(i, n):
                s = 0
                for K in range(i, j + 1):
                    s += arr[K]
                if s == k:
                    length = max(length, j - i + 1)
        return length


# Solution-2:
class Solution:
    def lenOfLongSubarr(self, arr, n, k):
        # Complete the function
        length = 0
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += arr[j]
                if s == k:
                    length = max(length, j - i + 1)
        return length


# Optimal Approach:
# Time Complexity: ~ O(2n)
# Space Complexity: O(1)


# Works only for positive numbers
# Solution-1:
class Solution:
    def lenOfLongSubarr(self, arr, n, k):
        # Complete the function
        pointer_left = 0
        pointer_right = 0
        sums = arr[0]
        largest_length = 0

        while pointer_right < n:
            if pointer_left <= pointer_right and sums > k:
                sums -= arr[pointer_left]
                pointer_left += 1

            if sums == k:
                largest_length = max(largest_length, pointer_right - pointer_left + 1)

            pointer_right += 1
            if pointer_right < n:
                sums += arr[pointer_right]

        return largest_length


# Solution-2
# Time Complexity: O(n)
# Space Complexity: O(n))
class Solution:
    def lenOfLongSubarr(self, arr, n, k):
        # Complete the function

        prefix_sum = 0
        max_len = 0
        sum_map = {}

        for i in range(n):
            prefix_sum += arr[i]

            if prefix_sum == k:
                max_len = i + 1

            if (prefix_sum - k) in sum_map:
                max_len = max(max_len, i - sum_map[prefix_sum - k])

            if prefix_sum not in sum_map:
                sum_map[prefix_sum] = i

        return max_len
