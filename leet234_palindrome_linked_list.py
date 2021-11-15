"""
Given the head of a singly linked list, return true if it is a palindrome.

# Method 1 - Use Array
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1
        return True

# Method 2 - Use Deque
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q: Deque = collections.deque()

        if not head:
            return True

        node = head
        # convert list
        while node is not None:
            q.append(node.val)
            node = node.next

        # check palindrome
        while len(q) > 1:
            if q.popLeft != q.pop():
                return False
        return True

# Method 3 - Fast ptr and Slow ptr
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head

        # find middle (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
"""
from typing import List
import collections

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# Method 4 - Fast ptr and Slow ptr (shorter version)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        prev = None
        fast = head
        slow = head

        # find middle (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            prev, prev.next, slow, fast = slow, prev, slow.next, fast.next.next

        if fast:
            slow = slow.next

        while prev and prev.val == slow.val:
            slow, rev = slow.next, prev.next
        return not prev



