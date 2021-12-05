"""
Given the root node of a binary search tree and two integers low and high,
return the sum of values of all nodes with a value in the inclusive range
[low, high].

# Method 1 - Brute Force
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0

        return (root.val if low <= root.val <= high else 0) + \
                self.rangeSumBST(root.left, low, high) + \
                self.rangeSumBST(root.right, low, high)

# Method 2 - DFS with pruning
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node: TreeNode):
            if not node:
                return 0
            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)

# Method 3 - Iterative DFS
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        stack, sum = [root], 0
        while stack:
            node = stack.pop()
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    sum += node.val
        return sum
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Method 4 - BFS
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        queue, sum = [root], 0
        while queue:
            node = queue.pop(0)
            if node:
                if node.val > low:
                    queue.append(node.left)
                if node.val < high:
                    queue.append(node.right)
                if low <= node.val <= high:
                    sum += node.val
        return sum

# Driver code
tree = TreeNode(10, TreeNode(5, TreeNode(3, None, None), TreeNode(7, None, None)),
                TreeNode(15, None, TreeNode(18, None, None)))
print(Solution().rangeSumBST(tree, 7, 15))