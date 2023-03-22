# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.parents = collections.deque([root])
        while self.parents[0].right: # complete with two children
            parent = self.parents.popleft()
            self.parents.extend([parent.left, parent.right])
        

    def insert(self, val: int) -> int:
        parent = self.parents[0]
        if parent.left:
            parent.right = TreeNode(val)
            self.parents.extend([parent.left, parent.right])
            self.parents.popleft()
        else:
            parent.left = TreeNode(val)
        return parent.val
        

    def get_root(self) -> Optional[TreeNode]:
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
