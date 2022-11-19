# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == key:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            if root.left and root.right:
                new_root = root.right # find smallest among the bigger number
                while new_root.left:
                    new_root = new_root.left
                # update the root and recursively delete the replacing node
                root.val = new_root.val
                root.right = self.deleteNode(root.right, root.val)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        
        return root
