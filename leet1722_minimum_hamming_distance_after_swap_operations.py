class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        dist = N = len(source)
        graph = [set() for i in range(N)]
        for s, e in allowedSwaps:
            graph[s].add(e)
            graph[e].add(s)
        seen = [0] * N

        # find numbers whose indices are connected together
        def dfs(start):
            seen[start] = 1
            found.append(start)
            for end in graph[start]:
                if not seen[end]:
                    dfs(end)
        
        for i in range(N):
            if seen[i]: 
                continue
            found = []
            dfs(i) 
            count1 = collections.Counter(source[pos] for pos in found)
            count2 = collections.Counter(target[pos] for pos in found)
            dist -= sum((count1 & count2).values())
        return dist
