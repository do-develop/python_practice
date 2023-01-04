# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)

        q = deque([root])
        while q and depth != 1:
            depth -= 1
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)
                # reached the level in depth - 1 ?
                if depth == 1:
                    curr.left = TreeNode(val, curr.left, None)
                    curr.right = TreeNode(val, None, curr.right)
        return root
