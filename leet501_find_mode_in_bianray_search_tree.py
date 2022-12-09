# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.mode = 0
        found = []
        count = collections.Counter()
        def traverse(node):
            if not node:
                return
            count[node.val] += 1
            self.mode = max(self.mode, count[node.val])
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        for k, v in count.items():
            if v == self.mode:
                found.append(k)
        return found
