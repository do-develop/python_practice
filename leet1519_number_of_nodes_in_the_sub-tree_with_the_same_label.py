class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        def dfs(node: int):
            cnt = Counter()
            if node not in seen:
                cnt[labels[node]] += 1
                seen.add(node)
                for child in graph.get(node, []):
                    cnt += dfs(child)
                ans[node] = cnt[labels[node]]
            return cnt
        
        graph, ans, seen = defaultdict(list), [0] * n, set()
        for u, v in edges:
            graph[u] += [v]
            graph[v] += [u]
        dfs(0)
        return ans
