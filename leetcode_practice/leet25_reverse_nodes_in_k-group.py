"""
Given the head of a linked list, reverse the nodes of the list k at a time, and
return the modified list. k is a positive integer and is less than or equal to
the length of the linked list. If the number of nodes is not a multiple of k
then left-out nodes, in the end, should remain as it is. You may not alter the
values in the list's nodes, only nodes themselves may be changed.
"""
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def ListToNode(ls: List[int]) -> ListNode:
    head = ListNode(ls[0])
    tmp = head
    for i in range(1, len(ls)):
        tmp.next = ListNode(ls[i])
        tmp = tmp.next
    return head

def NodeToList(head: ListNode) -> List[int]:
    ls = []
    while head:
        ls.append(head.val)
        head = head.next
    return ls

    
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)
        group_prv = dummy

        while True:
            kth = self.getKth(group_prv, k)
            if not kth:
                break
            group_next = kth.next

            # reverse group
            prv, cur = kth.next, group_prv.next

            while cur != group_next:
                tmp = cur.next
                cur.next = prv
                prv = cur
                cur = tmp

            tmp = group_prv.next
            group_prv.next = kth
            group_prv = tmp
        return dummy.next
            
    def getKth(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur            


# TEST
head = ListToNode([1,2,3,4,5])
k = 3
output = Solution().reverseKGroup(head, k)
print(NodeToList(output))
# Expected Output: [3,2,1,4,5]
