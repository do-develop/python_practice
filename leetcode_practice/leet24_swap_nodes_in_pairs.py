"""
Given a linked list, swap every two adjacent nodes and
return its head. You must solve the problem without
modifying the values in the list's nodes (i.e., only
nodes themselves may be changed.)

# Method 1 - Iterative version
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            # save ptrs
            nxtPair = head.next.next
            second = head.next

            # reverse this pair
            second.next = head
            head.next = nxtPair
            prev.next = second

            # update ptrs
            prev = head
            head = nxtPair
        return root.next

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Method 2 - Recursive version
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            # get the swapped return value
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head


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

l1 = to_linked_list([1, 2, 3, 4])

result = Solution().swapPairs(l1)
print(to_native_list(result))