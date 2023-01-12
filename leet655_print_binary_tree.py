# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def get_depth(node):
            if not node:
                return 0
            return max(get_depth(node.left), get_depth(node.right)) + 1

        def insert_value(node, lo, hi, depth=0):
            if not node:
                return
            mid = (lo + hi) // 2
            output[depth][mid] = str(node.val)
            insert_value(node.left, lo, mid, depth + 1)
            insert_value(node.right, mid, hi, depth + 1)          

        # get max depth
        max_depth = get_depth(root)
        columns = 2**max_depth - 1
        # initiate output
        output = [[""] * columns for _ in range(max_depth)]
        # insert value level by level
        insert_value(root, 0, columns)
        return output
Console
