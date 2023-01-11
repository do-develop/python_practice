# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        duplicates = []
        counter = {} # path:count

        def preorder(node, path: str):
            # serialize the tree to check duplicates
            if node is None:
                return '#'
            path += ','.join([str(node.val), preorder(node.left, path), preorder(node.right, path)])
            # increment counter to check duplicates
            if path in counter:
                counter[path] += 1
                if counter[path] == 2:
                    duplicates.append(node)
            else:
                counter[path] = 1
            return path
        preorder(root, '')
        return duplicates
