# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        l1ptr, l2ptr, i = list1, list2, 0
        # find the start of list2
        while True:
            if i == a - 1:
                athptr = l1ptr
            if i == b + 1:
                bthptr = l1ptr
                break
            l1ptr = l1ptr.next
            i += 1
        # find the end of list2
        while True:
            if l2ptr.next == None:
                break
            else:
                l2ptr = l2ptr.next
        athptr.next = list2
        l2ptr.next = bthptr
        return list1
