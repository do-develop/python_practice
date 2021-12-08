"""
Given an array of points where points[i] = [xi, yi] represents a point on the
X-Y plane and an integer k, return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance
(i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique
(except for the order that it is in).
"""

from typing import List
import heapq

# Min-heap approach
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for x, y in points:
            dist = ( x ** 2) + (y ** 2)
            heapq.heappush(min_heap, [dist, x, y])

        result = []

        for _ in range(k):
            dist, x, y = heapq.heappop(min_heap)
            result.append([x, y])

        return result



# Test
points = [[1, 3], [-2, 2]]
k = 1
print(Solution().kClosest(points, k))
