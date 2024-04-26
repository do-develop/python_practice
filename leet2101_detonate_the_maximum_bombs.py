class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        reachable = collections.defaultdict(set)
        N = len(bombs)
        # step 1 - for each source how much bombs will be detonated?
        for i in range(N): 
            xi, yi, ri = bombs[i] # source

            for j in range(N):
                if i == j:
                    continue
                xj, yj, rj = bombs[j]
                # is reachable from source (within radius?)
                if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                    reachable[i].add(j)
                    
        # step 2 - how to count chain detonation
        def dfs(n, seen):
            if n in seen:
                return
            seen.add(n)
            for nxt in reachable[n]:
                dfs(nxt, seen)
                
        # step 3 - count chains for each bomb
        count = 0
        for i in range(N):
            seen = set()
            dfs(i, seen)
            count = max(count, len(seen))
        return count

