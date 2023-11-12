class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for x, y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)

        # find the end node
        root = None
        for num in graph:
            if len(graph[num]) == 1:
                root = num
                break
        
        def dfs(node, prev, ans):
            ans.append(node)
            for neigh in graph[node]:
                if neigh != prev:
                    dfs(neigh, node, ans)
        
        ans = []
        dfs(root, None, ans)
        return ans
