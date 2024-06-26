# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = defaultdict(TreeNode)
        has_parents = set()

        for parent, child, is_left in descriptions:
            if child not in nodes:
                nodes[child] = TreeNode(child)
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            
            if is_left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
            
            has_parents.add(child)
        
        for node_key in nodes.keys():
            if node_key not in has_parents:
                return nodes[node_key]
