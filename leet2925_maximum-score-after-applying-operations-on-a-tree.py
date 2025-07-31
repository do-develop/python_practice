class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        # find minimum unavoidable loss then subtract from total to get the answer
        total = sum(values)
        graph = defaultdict(list)
        
        # construct adjacency list for the tree
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs_helper(node):
            # base case - leaf node then just return its value
            if not graph[node]:
                return values[node]
            
            mini = 0
            for n in graph[node]:
                graph[n].remove(node)
                mini += dfs_helper(n)

            if mini < values[node]:
                return mini
            else:
                return values[node]

        return total - dfs_helper(0)
        
