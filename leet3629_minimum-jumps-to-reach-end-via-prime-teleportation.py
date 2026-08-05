MX = 1_000_001
sieve = [[] for _ in range(MX)]
for i in range(2, MX):
    if not sieve[i]:
        for j in range (i, MX, i):
            sieve[j].append(i)

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        N = len(nums)
        edges = defaultdict(list)
        for i, v in enumerate(nums):
            if len(sieve[v]) == 1:
                edges[v].append(i)

        res = 0
        seen = [False] * N
        seen[-1] = True
        q = [N-1]
        while True:
            q2 = []
            for i in q:
                if i == 0:
                    return res
                if i > 0 and not seen[i - 1]:
                    seen[i-1] = True
                    q2.append(i-1)
                if i < N - 1 and not seen[i + 1]:
                    seen[i+1] = True
                    q2.append(i+1)
                for p in sieve[nums[i]]:
                    for j in edges[p]:
                        if not seen[j]:
                            seen[j] = True
                            q2.append(j)
                    edges[p].clear()
            
            q = q2
            res += 1
