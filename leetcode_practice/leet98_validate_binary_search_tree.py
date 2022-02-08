"""
Given the root of a binary tree, determine if it is a valid binary search tree
(BST).A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's
key. The right subtree of a node contains only nodes with keys greater than the
node's key. Both the left and right subtrees must also be binary search trees.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(root, left, right) -> bool:
            if not root:
                return True
            if not(root.val > left and root.val < right):
                return False
            return (valid(root.left, left, root.val) and
                    valid(root.right, root.val, right))
        return valid(root, float("-inf"), float("inf"))
        


# TEST
root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
print(Solution().isValidBST(root))
# Output: false --> Explanation: The root node's value is 5 but its right child's value is 4.
