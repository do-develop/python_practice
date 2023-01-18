# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.length = 0

        def get_length(node):
            if not node:
                return 0
            left_len = get_length(node.left)
            right_len = get_length(node.right)
            left_edge = right_edge = 0
            if node.left and node.left.val == node.val:
                left_edge = left_len + 1
            if node.right and node.right.val == node.val:
                right_edge = right_len + 1
            self.length = max(self.length, left_edge + right_edge)
            return max(left_edge, right_edge)
        
        get_length(root)
        return self.length
