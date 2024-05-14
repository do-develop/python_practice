# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # slow and fast pointer technique to get to the mid node
        # and reverse the first half
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        max_pair = 0
        # pair from inside to outside
        while slow:
            max_pair = max(max_pair, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        return max_pair
