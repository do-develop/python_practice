class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def improvement(a, b):
            return (a + 1)/(b + 1) - a/b

        max_heap = []
        for a, b in classes:
            a, b = a * 1.0, b * 1.0
            max_heap.append((-improvement(a, b), a, b))
        heapq.heapify(max_heap)

        # greedily use the one with the maximum improvement
        for _ in range(extraStudents):
            _, a, b = heapq.heappop(max_heap)
            heapq.heappush(max_heap, (-improvement(a + 1, b + 1), a + 1, b + 1))

        return sum(a/b for _, a, b in max_heap) / len(classes)
