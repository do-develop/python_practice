# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        has_null = False
        q = [root]
        while q:
            node = q.pop(0)
            if not node:
                has_null = True
                continue
            if has_null: 
                return False
            q.append(node.left)
            q.append(node.right)
        return True
