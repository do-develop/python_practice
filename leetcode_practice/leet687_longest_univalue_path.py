"""
Given the root of a binary tree, return the length of the longest path,
where each node in the path has the same value. This path may or may not
pass through the root.

The length of the path between two nodes is represented by the number
of edges between them.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    result: int = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
            # update the result with the sum of left and right length
            self.result = max(self.result, left + right)
            # Return the max from left and right to upper node
            # since only one side path is valid
            return max(left, right)

        dfs(root)
        return self.result

# Driver code
root = TreeNode()
root.val = 4
root.left = TreeNode(4, TreeNode(1, None, None), TreeNode(4, None, None))
root.right = TreeNode(4, None, TreeNode(5, None, None))

print(Solution().longestUnivaluePath(root))