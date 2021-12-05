"""
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree
such that every key of the original BST is changed to the original key plus
the sum of all keys greater than the original key in BST.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.val),
        if self.right:
            self.right.printTree()

class Solution:
    value: int = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right)
            self.value += root. val
            root.val = self.value
            self.bstToGst(root.left)

        return root

# Driver Code
tree = TreeNode(4, TreeNode(1, TreeNode(0, None, None), TreeNode(2, None, TreeNode(3, None, None))),
                TreeNode(6, TreeNode(5, None, None), TreeNode(7, None, TreeNode(8, None, None))))

Solution().bstToGst(tree)
tree.printTree()