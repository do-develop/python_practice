# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find_path(node:TreeNode, val:int, path:List[str]) -> bool:
            if node.val == val:
                return True
            if node.left and find_path(node.left, val, path):
                path += "L"
            elif node.right and find_path(node.right, val, path):
                path += "R"
            return path
        
        spath, dpath = [], []
        find_path(root, startValue, spath)
        find_path(root, destValue, dpath)

        while len(spath) and len(dpath) and spath[-1] == dpath[-1]:
            spath.pop()
            dpath.pop()
        
        return "".join("U" * len(spath)) + "".join(reversed(dpath))
