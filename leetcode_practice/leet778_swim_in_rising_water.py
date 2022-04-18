"""
You are given an n x n integer matrix grid where each value grid[i][j]
represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t.
You can swim from a square to another 4-directionally adjacent square if and
only if the elevation of both squares individually are at most t. You can swim
infinite distances in zero time. Of course, you must stay within the boundaries
of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).
"""
# modified dijkstra's algo (BFS with minheap)
# keep max_height instead of Weight/distance

from typing import List
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visited = set()
        min_heap = [[grid[0][0], 0, 0]] # (max_height, r, c)
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        
        visited.add((0,0))
        while min_heap:
            t, r, c = heapq.heappop(min_heap)

            if r == N-1 and c == N-1:
                return t

            for dr, dc in directions:
                nei_row, nei_col = r + dr, c + dc
                if (nei_row < 0 or nei_col < 0 or
                    nei_row == N or nei_col == N or
                    (nei_row, nei_col) in visited):
                    continue
                visited.add((nei_row, nei_col))
                heapq.heappush(min_heap, [max(t, grid[nei_row][nei_col]), nei_row, nei_col])

        

# TEST
grid = [[0,1,2,3,4],
        [24,23,22,21,5],
        [12,13,14,15,16],
        [11,17,18,19,20],
        [10,9,8,7,6]]
print(Solution().swimInWater(grid))
"""
Output: 16
Explanation: The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.


grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
"""
