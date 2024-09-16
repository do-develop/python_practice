# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        movement = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = [[-1 for _ in range(n)] for _ in range(m)]

        r, c = 0, 0
        cur_d = 0

        while head:
            res[r][c] = head.val
            newr = r + movement[cur_d][0]
            newc = c + movement[cur_d][1]

            if(
                min(newr, newc) < 0 
                or newr >= m
                or newc >= n
                or res[newr][newc] != -1
            ):
                cur_d = (cur_d + 1) % 4

            r += movement[cur_d][0]
            c += movement[cur_d][1]
            head = head.next
            
        return res
