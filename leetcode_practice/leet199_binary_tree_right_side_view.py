"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
"""
from typing import List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        result = []
        q = collections.deque([root])
        # Add elements on the same level in q (BFS)
        while q:
            right_side = None
            qlen = len(q)

            for i in range(qlen):
                node = q.popleft()
                if node:
                    right_side = node
                    q.append(node.left)
                    q.append(node.right)

            if right_side:
                result.append(right_side.val)

        return result




# TEST
root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
print(Solution().rightSideView(root))  # expected output: [1,3,4]
