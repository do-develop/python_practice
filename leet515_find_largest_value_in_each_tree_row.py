# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = [root]
        length = len(q)
        ans = []

        while length:
            max_val = max([node.val for node in q])
            ans.append(max_val)
            # save next level info
            temp = []
            for node in q:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            # move on to the next level
            q = temp
            length = len(q)
        
        return ans