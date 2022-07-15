"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two
given nodes in the BST. According to the definition of LCA on Wikipedia: “The
lowest common ancestor is defined between two nodes p and q as the lowest node
in T that has both p and q as descendants (where we allow a node to be a
descendant of itself).”
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur




# TEST
root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))),
         TreeNode(8, TreeNode(7), TreeNode(9)))

p = TreeNode(2)
q = TreeNode(8)
print(Solution().lowestCommonAncestor(root, p, q).val)
# expected output: 6
