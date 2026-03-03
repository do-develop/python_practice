# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def dfs(node):
            if not node:
                return 0
            left_h = dfs(node.left)
            right_h = dfs(node.right)
            if left_h != right_h:
                return -1    
            arr.append(left_h + right_h + 1)
            return left_h + right_h + 1
        
        dfs(root)
        if k > len(arr):
            return -1

        return nlargest(k, arr)[k-1]
