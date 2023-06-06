# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        l = r = 0
        def count(node):
            nonlocal l, r
            total = 0
            if node: 
                l_count, r_count = count(node.left), count(node.right)
                if node.val == x: 
                    l, r = l_count, r_count # remember subtree count
                total += l_count + r_count + 1
            return total
        s = count(root) 
        p = s-l-r-1 # parent = total - left - right - first player choice
        return l+r < p or l+p < r or r+p < l
