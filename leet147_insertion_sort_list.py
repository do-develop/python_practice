"""
Given the head of a singly linked list, sort the list using
insertion sort, and return the sorted list's head.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def print_list(self):
        temp = self
        while temp:
            print(temp.val)
            temp = temp.next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur = parent = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            if head and cur.val> head.val:
                cur = parent
        return parent.next

root = ListNode(4)
root.next = ListNode(2)
root.next.next = ListNode(1)
root.next.next.next = ListNode(3)

sorted_list = Solution().insertionSortList(root)
sorted_list.print_list()