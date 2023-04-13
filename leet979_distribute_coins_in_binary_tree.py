# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        # check each leaf has any excess coins
        # the absolute value of the excess count is
        # the number of moves to distribute the coins
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.ans += abs(left) + abs(right)
            return node.val + left + right - 1 # excess = abs(number_of_coins - 1)
        dfs(root)
        return self.ans
