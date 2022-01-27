"""
You are given two non-empty linked lists representing two
non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two
numbers and return the sum as a linked list.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode()
        head = root  # pointer
        carry = 0
        while l1 or l2 or carry:  # or carry takes care of the edge cases
            sum = 0

            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next

def to_linked_list(iterable):
    head = None
    for val in reversed(iterable):
        head = ListNode(val, head)
    return head

def to_native_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst

l1 = to_linked_list([2, 4, 3])
l2 = to_linked_list([5, 6, 4])
result = Solution().addTwoNumbers(l1, l2)
print(to_native_list(result))