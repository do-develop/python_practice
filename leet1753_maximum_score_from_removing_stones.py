class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        queue = [-a, -b, -c]
        heapq.heapify(queue)
        count = 0

        while True:
            if queue[0] != 0 and queue[1] != 0:
                count += 1
                first = heapq.heappop(queue)
                second = heapq.heappop(queue)
                heapq.heappush(queue, first + 1)
                heapq.heappush(queue, second + 1)
            else:
                break
        return count
