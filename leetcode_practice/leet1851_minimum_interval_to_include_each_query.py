"""
You are given a 2D integer array intervals, where intervals[i] = [lefti, righti]
describes the ith interval starting at lefti and ending at righti (inclusive).
The size of an interval is defined as the number of integers it contains, or
more formally righti - lefti + 1.

You are also given an integer array queries. The answer to the jth query is the
size of the smallest interval i such that lefti <= queries[j] <= righti. If no
such interval exists, the answer is -1.

Return an array containing the answers to the queries.
"""
from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        min_heap = []
        res, i = {}, 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l,r = intervals[i]
                heapq.heappush(min_heap, (r-l+1, r))
                i += 1
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            res[q] = min_heap[0][0] if min_heap else -1
                
        return [res[q] for q in queries]
                  

              


#TEST
intervals = [[1,4],[2,4],[3,6],[4,4]]
queries = [2,3,4,5]
print(Solution().minInterval(intervals,queries))
# expected output: [3,3,1,4]
