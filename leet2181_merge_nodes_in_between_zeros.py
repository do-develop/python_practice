# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        total = 0

        while head:
            total += head.val
            if head.val == 0 and total:
                stack.append(total)
                total = 0
            head = head.next

        prev = None
        while stack:
            head = ListNode(stack.pop())
            head.next = prev
            prev = head
        return head
