# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        freq_sum = {}
        self.max_freq = 0

        def find_tree_sum(node):
            if not node:
                return 0
            return node.val + find_tree_sum(node.left) + find_tree_sum(node.right)
        
        def traverse_tree(node): # preorder
            if not node:
                return
            # find the current node's sum
            curr_sum = find_tree_sum(node)
            freq_sum[curr_sum] = freq_sum.get(curr_sum, 0) + 1
            self.max_freq = max(self.max_freq, freq_sum[curr_sum])
            # recursive call to visit all node
            traverse_tree(node.left)
            traverse_tree(node.right)

        # call the recursive function
        traverse_tree(root)
        max_freq_sums = []
        for sum in freq_sum:
            if freq_sum[sum] == self.max_freq:
                max_freq_sums.append(sum)
        return max_freq_sums
