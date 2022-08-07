"""
A linked list of length n is given such that each node contains an additional
random pointer, which could point to any node in the list, or null. Construct
a deep copy of the list. The deep copy should consist of exactly n brand new
nodes, where each new node has its value set to the value of its corresponding
original node. Both the next and random pointer of the new nodes should point
to new nodes in the copied list such that the pointers in the original list and
copied list represent the same list state. None of the pointers in the new list
should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random
--> Y, then for the corresponding two nodes x and y in the copied list, x.random
--> y.

Return the head of the copied linked list.
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: Node = None, random: Node = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        oldToCopy = { None: None}
        # make copies
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        # set pointers
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]



head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# expected output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
