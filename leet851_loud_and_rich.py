class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        richer_nei = collections.defaultdict(list)
        for i, j in richer: # make a graph
            richer_nei[j].append(i)
        # result variable
        least_quiet = [None] * len(quiet)

        def dfs(node):
            # find least queit person in this subtree
            if least_quiet[node] is None:
                least_quiet[node] = node
                for nei in richer_nei[node]:
                    cand = dfs(nei)
                    if quiet[cand] < quiet[least_quiet[node]]:
                        least_quiet[node] = cand
            return least_quiet[node]
        
        return map(dfs, range(len(quiet)))

