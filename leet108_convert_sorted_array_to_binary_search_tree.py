"""
Given an integer array nums where the elements are sorted in
ascending order, convert it to a height-balanced BST.
A height-balanced binary tree is a binary tree in which the depth
of the two subtrees of every node never differs by more than one.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def printTree(self):
        print(self.val)
        if self.left:
            self.left.printTree()
        if self.right:
            self.right.printTree()

from typing import List

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root

# Driver Code
tree = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
tree.printTree()