"""
Given the root of a binary tree, invert the tree, and return its root.

# Method 1 - Recursive calls
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        else:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root

# Method 2 - Iterative BFS
import collections
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.val),
        if self.right:
            self.right.printTree()

# Method 3 - Iterative DFS, post-order
import collections
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = collections.deque([root])

        while stack:
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)
                node.left, node.right = node.right, node.left

        return root


# Driver Code
root = TreeNode(4, TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)),
                TreeNode(7, TreeNode(6, None, None), TreeNode(9, None, None)))
root.printTree()
Solution().invertTree(root)
root.printTree()