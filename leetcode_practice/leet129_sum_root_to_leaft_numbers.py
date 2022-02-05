"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        def dfs(cur, sum):
            if not cur:
                return 0

            sum = sum * 10 + cur.val
            # leaf node?
            if not cur.left and not cur.right:
                return sum
            return dfs(cur.left, sum) + dfs(cur.right, sum)

        return dfs(root, 0)


# Test
root = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
print(Solution().sumNumbers(root))  # output: 1026
