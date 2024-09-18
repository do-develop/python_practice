# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        def evaluate(node):
            left, right = False, False
            if node.left:
                left = evaluate(node.left)
            if node.right:
                right = evaluate(node.right)
            if node.val == 2:
                return left or right
            if node.val == 3:
                return left and right
            return node.val == 1
        return evaluate(root)
