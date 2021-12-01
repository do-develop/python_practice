"""
Given the root of a binary tree, return the length of the diameter
of the tree.
The diameter of a binary tree is the length of the longest path between
any twonodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of
edges between them.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
"""
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def get_length(node):
            left_length = right_length = 0
            if node.left:
                left_length = get_length(node.left) + 1
            if node.right:
                right_length = get_length(node.right) + 1
            res.append(left_length + right_length)

            return max(left_length, right_length)

        res = [0]
        if root:
            get_length(root)

        return max(res)
"""      

class Solution(object):
    longest: int = 0
    def diameterOfBinaryTree(self, root):

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            self.longest = max(self.longest, left+right)
            return 1 + max(left, right)
            
        dfs(root)
        return self.longest

# Driver Code
root = TreeNode()
root.left = TreeNode()
root.right = TreeNode()
root.left.left = TreeNode()
root.left.right = TreeNode()

print(Solution().diameterOfBinaryTree(root))
