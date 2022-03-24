"""
Given a binary tree root, a node X in the tree is named good if in the path
from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_val):
            if not node:
                return 0

            count = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)
            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)
            return count
        
        return dfs(root, root.val)
            





# TEST
root = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
print(Solution().goodNodes(root))
# expected output: 4
