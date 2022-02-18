"""
Given the head of a linked list, remove the nth node from the end of the list
and return its head.
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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left, right = dummy, head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        # remove the node
        left.next = left.next.next

        return dummy.next



# TEST
head = ListToNode([1,2,3,4,5])
n = 2
output = Solution().removeNthFromEnd(head, n)
print(NodeToList(output))  # Expected Output: [1,2,3,5]
