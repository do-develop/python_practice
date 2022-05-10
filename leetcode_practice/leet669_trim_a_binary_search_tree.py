"""
Given the root of a binary search tree and the lowest and highest boundaries
as low and high, trim the tree so that all its elements lies in [low, high].
Trimming the tree should not change the relative structure of the elements that
will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change
depending on the given bounds.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def printTree(self):
        node = self
        if node:
            print(node.val)
            if node.left: node.left.printTree()
            if node.right: node.right.printTree()

class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return None

        if root.val > high:
            return self.trimBST(root.left, low, high)
        if root.val < low:
            return self.trimBST(root.right, low, high)

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root


# TEST
root = TreeNode(3, TreeNode(0, None, TreeNode(2, TreeNode(1), None)), TreeNode(4))
low = 1
high = 3
trimmed = Solution().trimBST(root, low, high)
trimmed.printTree()
#Output: [3,2,null,1]
