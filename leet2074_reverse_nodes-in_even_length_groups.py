# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        connector = None
        curr = head
        curr_count = group_count = 1

        def reverse_between(sentinel, n):
            prev = sentinel
            curr = sentinel.next
            tail = sentinel.next

            for _ in range(n):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            
            sentinel.next = prev
            tail.next = curr
            return tail
        
        while curr:
            if group_count == curr_count or not curr.next:
                if curr_count % 2 == 0:
                    curr = reverse_between(connector, curr_count)
                connector = curr
                group_count += 1
                curr_count = 0

            curr_count += 1
            curr = curr.next
        return head
