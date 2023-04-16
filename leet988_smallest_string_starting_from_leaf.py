# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.ans = "~"

        def dfs(node, word):
            if node:
                word.append(chr(node.val + ord('a')))
                if not node.left and not node.right:
                    self.ans = min(self.ans, "".join(reversed(word)))
                
                dfs(node.left, word)
                dfs(node.right, word)
                word.pop()
        dfs(root, [])
        return self.ans
