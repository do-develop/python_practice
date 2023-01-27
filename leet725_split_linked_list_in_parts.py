# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # count the length of the linked list
        curr, length = head, 0
        while curr:
            curr = curr.next
            length += 1
        
        # determine the length of each part
        part_size, remain_size = length // k, length % k
        res = [part_size + 1] * remain_size + [part_size] * (k  - remain_size)
        
        # split up the list
        prev, curr = None, head
        for idx, size in enumerate(res):
            # split point? then split
            if prev:
                prev.next = None
            res[idx] = curr
            for i in range(size):
                prev, curr = curr, curr.next
        return res
