"""
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root. The length of
a path between two nodes is represented by the number of edges between them.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        result = [0]
        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            result[0] = max(result[0], left+right)

            return max(left, right) + 1
        dfs(root)
        return result[0]
        


root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(Solution().diameterOfBinaryTree(root))
# expected output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
