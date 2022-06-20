"""
The thief has found himself a new place for his thievery again. There is only
one entrance to this area, called root. Besides the root, each house has one
and only one parent house. After a tour, the smart thief realized that all
houses in this place form a binary tree. It will automatically contact the
police if two directly-linked houses were broken into on the same night. Given
the root of the binary tree, return the maximum amount of money the thief can
rob without alerting the police.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(root):
            # base case
            if not root:
                return [0, 0]

            leftPair = dfs(root.left)
            rightPair = dfs(root.right)

            withRoot = root.val + leftPair[1] + rightPair[1]
            withoutRoot = max(leftPair) + max(rightPair)

            return[withRoot, withoutRoot]
        
        return max(dfs(root))


# TEST
root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(3)), TreeNode(5, None, TreeNode(1)))
print(Solution().rob(root))
# expected output 9 (= 4 + 5)
