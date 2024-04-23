# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return

        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            if fast.next.next:
                fast = fast.next.next
            else:
                fast = fast.next
                
        # Now slow is pointing mid node, remove it!
        if slow.next:
            slow.val = slow.next.val
            slow.next = slow.next.next
        else: # Edge case - there is only one node left
            head.next = None

        return head
