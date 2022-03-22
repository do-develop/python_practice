"""
You are given an array points representing integer coordinates of some points
on a 2D-plane, where points[i] = [xi, yi]. The cost of connecting two points
[xi, yi] and [xj, yj] is the manhattan distance between them:
|xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected
if there is exactly one simple path between any two points.
"""
#Kruskal Algorithm

from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def calculateDistance(p1: List[int], p2: List[int]) -> int:
            dist1 = abs(p1[0] - p2[0])
            dist2 = abs(p1[1] - p2[1])
            return dist1 + dist2

        def find_parent(parent, x) -> int:
            if parent[x] == x:
                return x
            return find_parent(parent, parent[x])

        def make_union(parent, a, b):
            a = find_parent(parent, a)
            b = find_parent(parent, b)
            if a > b:
                parent[b] = a
            else:
                parent[a] = b

        # (distance, pnt1_idx, pnt2_idx)
        graph = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                graph.append((calculateDistance(points[i], points[j]), i, j))
        graph.sort()  # sort by distance

        # declare and initialise parent
        parent =[0] * len(points)
        for i in range(len(points)):
            parent[i] = i
        
        # perform Kruskal algorithm
        connect_cost = 0
        for data in graph:
            cost, p1, p2 = data

            if find_parent(parent, p1) != find_parent(parent, p2):
                make_union(parent, p1, p2)
                connect_cost += cost
        return connect_cost
        
        

# TEST
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(Solution().minCostConnectPoints(points))
# expected output: 20
"""
points = [[3,12],[-2,5],[-4,1]]
Output: 18
"""
