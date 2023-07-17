# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        curr = [root]
        while curr:
            prev = curr
            temp = []
            for parent in curr:
                for child in [parent.left, parent.right]:
                    if child:
                        temp.append(child)
            curr = temp
        # if curr level is empty prev level is the deepest
        return sum(node.val for node in prev)
