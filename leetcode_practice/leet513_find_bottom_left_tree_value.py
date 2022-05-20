"""
Given the root of a binary tree, return the leftmost value in the last row of
the tree.
"""
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q = deque([root])

        while q:
            node = q.popleft()

            if node.right: q.append(node.right)
            if node.left: q.append(node.left)
        return node.val
        
