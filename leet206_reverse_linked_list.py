"""
Given the head of a singly linked list, reverse the list,
and return the reversed list.

# Method 1 - Iterative approach T:O(N) M:O(1)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Method 2 - Recursive approach T:O(N) M:O(N)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            nxt, node.next = node.next, prev
            return reverse(next, node)
        return reverse(head)


def to_native_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst

node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)

result = Solution().reverseList(node)
print(to_native_list(result))