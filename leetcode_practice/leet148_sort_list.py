"""
Given the head of a linked list, return the list after sorting it in ascending order.


# merge sort approach
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # split the list into two halves
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp
        
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)

    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
                

    def merge(self, left, right):
        tail = dummy = ListNode()
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                 tail.next = right
                 right = right.next
            tail = tail.next
        if left:
            tail.next = left
        if right:
            tail.next = right
            
        return dummy.next

# library sort approach
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        list_nums = []

        while head != None:
            list_nums.append(head.val)
            head = head.next

        list_nums = sorted(list_nums)

        answerList = ListNode(0)

        result = answerList

        for num in list_nums:
            answerList.next = ListNode(num)
            answerList = answerList.next

        return result.next


# merge sort with better space complexity
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head

        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.mergeTwoLists(l1, l2)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# merge sort with better space complexity
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head

        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.mergeTwoLists(l1, l2)



        
# Test
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(5)
head.next.next.next = ListNode(1)
sorted = Solution().sortList(head)

while sorted:
    print(sorted.val, end=" ")
    sorted = sorted.next
