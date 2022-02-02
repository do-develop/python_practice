"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
"""
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def ListToNode(ls: List[int])-> ListNode:
    head = ListNode(ls[0])
    nxt = head
    for i in range(1, len(ls)):
        nxt.next = ListNode(ls[i])
        nxt = nxt.next
    return head

def NodeToList(head: ListNode)-> List[int]:
    ls = []
    while head:
        ls.append(head.val)
        head = head.next
    return ls

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(next=head)
        prv, cur = dummy, head

        while cur:
            if cur.val == val:
                prv.next = cur.next
            else:
                prv = cur
            cur = cur.next
        return dummy.next

# TEST
head = ListToNode([1,2,6,3,4,5,6])
val = 6
output = Solution().removeElements(head, val)
print(NodeToList(output))  # Expected Output: [1,2,3,4,5]
