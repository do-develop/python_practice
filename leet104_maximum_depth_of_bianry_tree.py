"""
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along
the longest path from the root node down to the farthest leaf node.

# Method 1 - Recursive DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Method 2 - BFS
import collections

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        level = 0
        q = collections.deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Method 3 - Iterative DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = [[root, 1]]
        result = 0
        
        while stack:
            node, depth = stack.pop()

            if node:
                result = max(result, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])

        return result
        

node4 = TreeNode(6, None, None)
node2 = TreeNode(2, None, None)
node3 = TreeNode(4, None, node4)
node1 = TreeNode(3, node2, node3)

print(Solution().maxDepth(node1))
        
