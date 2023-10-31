class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        # using heap:
        # the first element - how many days the apple in that batch will stay fresh. 
        # the second element - how many apples are left in the same batch which can be consumed.
        eaten, day, N = 0, 0, len(apples)
        heap = []
        while day < N or heap:
            # only push to heap when there is valid day and the apple is still fresh
            if day < N and apples[day] > 0:
                heappush(heap, [day + days[day], apples[day]])
            # remove the batch with rotten apples or if it is empty
            while heap and (heap[0][0] <= day or heap[0][1] <= 0):
                heappop(heap)
            if heap:
                heap[0][1] -= 1
                eaten += 1
            day += 1
        return eaten
