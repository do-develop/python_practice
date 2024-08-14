# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0

        def postorder(node):
            if node is None:
                return [0, 0]

            left = postorder(node.left)
            right = postorder(node.right)
            node_sum = left[0] + right[0] + node.val
            node_cnt = left[1] + right[1] + 1

            if (node.val == node_sum // node_cnt):
                self.count += 1
            
            return [node_sum, node_cnt]
        
        postorder(root)
        return self.count
