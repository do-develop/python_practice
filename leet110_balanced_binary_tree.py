"""
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every
node differ in height by no more than 1.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def dfs(root):
            # base case
            if not root:
                return 0

            left, right = dfs(root.left), dfs(root.right)
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            return max(left, right) + 1

        return dfs(root) != -1

# Driver Code
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(3)

print(Solution().isBalanced(root))
    
        
