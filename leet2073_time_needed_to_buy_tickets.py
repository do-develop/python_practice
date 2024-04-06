class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        N = len(tickets)
        total = 0

        while tickets[k]:
            for i in range(N):
                if tickets[k] < 1:
                    return total
                if tickets[i] < 1:
                    continue
                total += 1
                tickets[i] -= 1
        return total
