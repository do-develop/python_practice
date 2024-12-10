class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        head = costs[:candidates]
        tail = costs[max(candidates, len(costs) - candidates):]
        heapify(head)
        heapify(tail)
        answer = 0
        next_head, next_tail = candidates, len(costs) - candidates - 1

        for _ in range(k):
            if not tail or (head and head[0] <= tail[0]):
                answer += heappop(head)
                if next_head <= next_tail:
                    heappush(head, costs[next_head])
                    next_head += 1
            else:
                answer += heappop(tail)
                if next_head <= next_tail:
                    heappush(tail, costs[next_tail])
                    next_tail -= 1
        return answer
