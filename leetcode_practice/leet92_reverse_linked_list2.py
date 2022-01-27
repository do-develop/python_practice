"""
Given the head of a singly linked list and two integers
left and right where left <= right, reverse the nodes of
the list from position left to position right, and return
the reversed list.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0, head)

        # 1) reach node at position "left"
        left_prev, cur = dummy, head
        for i in range(left - 1):
            left_prev, cur = cur, cur.next

        # now cur="left", left_prev = "node before left"
        # 2) reverse from left to right
        prev = None
        for i in range(right - left + 1):
            tmp_next = cur.next  # not to lose the link to the node after cur
            cur.next = prev
            prev, cur = cur, tmp_next

        # 3) update pointers
        left_prev.next.next = cur  # cur is node after "right"
        left_prev.next = prev      # prev is "right"

        return dummy.next


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


if __name__ == '__main__':
    list1 = to_linked_list([1,2,3,4,5])

    result = Solution().reverseBetween(list1, 2, 4)
    print(to_native_list(result))




