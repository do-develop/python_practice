"""
Given the head of a singly linked list, group all the nodes
with odd indices together followed by the nodes with even
indices, and return the reordered list.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # handle exception
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        # process odd/even nodes
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        # last odd node will be connected to the even_head
        odd.next = even_head
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

list1 = to_linked_list([2, 1, 3, 5, 6, 4, 7])

result = Solution().oddEvenList(list1)
print(to_native_list(result))