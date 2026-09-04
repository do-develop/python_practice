class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        N = len(arrivals)
        count = defaultdict(int)
        dq = deque() # (day, type) for kept items, in increasing order
        discards = 0

        for i in range(1, N + 1):
            while dq and dq[0][0] <= i - w:
                _, t_old = dq.popleft()
                count[t_old] -= 1

            t = arrivals[i - 1]
            if count[t] < m:
                count[t] += 1
                dq.append((i, t))
            else:
                discards += 1
        
        return discards
