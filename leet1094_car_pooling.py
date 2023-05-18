class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # use min heap, O(nlogn) solution
        trips.sort(key = lambda t: t[1]) # sort by starting point
        min_heap = []
        cur_pass = 0 # current passengers
        for t in trips:
            num_pass, start, end = t
            while min_heap and min_heap[0][0] <= start:
                cur_pass -= min_heap[0][1]
                heapq.heappop(min_heap)

            cur_pass += num_pass
            if cur_pass > capacity:
                return False
            heapq.heappush(min_heap, [end, num_pass])
        return True


