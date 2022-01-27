"""
You are given two binary trees root1 and root2.
Imagine that when you put one of them to cover the other, some nodes
of the two trees are overlapped while the others are not. You need to
merge the two trees into a new binary tree. The merge rule is that if
two nodes overlap, then sum node values up as the new value of the
merged node. Otherwise, the NOT null node will be used as the node of
the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.
"""

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
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 and root2:
            v1 = root1.val
            v2 = root2.val
            sum_node = TreeNode(v1 + v2)
            sum_node.left = self.mergeTrees(root1.left, root2.left)
            sum_node.right = self.mergeTrees(root1.right, root2.right)
            return sum_node
        else:
            return root1 or root2

# Driver Code
root1 = TreeNode(1, TreeNode(3, TreeNode(5, None, None), None), TreeNode(2, None, None))
root2 = TreeNode(2, TreeNode(1, None, TreeNode(4, None, None)), TreeNode(3, None, TreeNode(7, None, None)))

root3 = Solution().mergeTrees(root1, root2)
root3.printTree()

