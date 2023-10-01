# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        level = 0
        while q:
            n = len(q)
            is_even_level = level % 2 == 0
            if is_even_level:
                if q[0].val % 2 == 0:
                    return False
            elif q[0].val % 2 != 0:
                return False
            
            for i in range(1, n):
                if is_even_level:
                    if q[i].val % 2 == 0 or q[i].val <= q[i-1].val:
                        return False
                elif q[i].val % 2 != 0 or q[i].val >= q[i-1].val:
                    return False
            
            for i in range(n):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            level += 1
        return True
