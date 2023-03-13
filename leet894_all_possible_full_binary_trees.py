# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # optimise the brute force solution with caching
        cache = {0: [], 1:[TreeNode()]} # map n : list of FBT

        # return the list of full binary tree with n nodes
        def backtrack(n):
            if n in cache:
                return cache[n]
            
            res = []
            for l in range(n): # 0 to n- 1 nodes
                r = n - 1 - l
                left_tree, right_tree = backtrack(l), backtrack(r)
                # all combinations
                for t1 in left_tree:
                    for t2 in right_tree:
                        res.append(TreeNode(0, t1, t2))
            cache[n] = res
            return res
        return backtrack(n)
        
