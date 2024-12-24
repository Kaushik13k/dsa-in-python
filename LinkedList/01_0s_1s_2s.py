# https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1?utm_source=youtube


# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    # Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        if not head or not head.next:
            return head

        temp = head
        zeros_head = Node(-1)
        ones_head = Node(-1)
        twos_head = Node(-1)

        zero = zeros_head
        one = ones_head
        two = twos_head

        while temp:
            if temp.data == 0:
                zero.next = temp
                zero = temp
            elif temp.data == 1:
                one.next = temp
                one = temp
            else:
                two.next = temp
                two = temp
            temp = temp.next

        zero.next = ones_head.next if ones_head.next else twos_head.next
        one.next = twos_head.next
        two.next = None

        return zeros_head.next
