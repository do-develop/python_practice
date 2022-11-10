"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # dfs approach --> need to traverse as deep as possible
        if not head:
            return head
        stack, ordered = [head], []
        
        while stack:
            node = stack.pop()
            ordered.append(node)
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child) # child will be visited before the next neighbor
        
        for i in range(len(ordered) - 1):
            ordered[i+1].prev = ordered[i]
            ordered[i].next = ordered[i+1]
            ordered[i].child = None
            
        return ordered[0]
