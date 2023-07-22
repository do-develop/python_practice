class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        neighbors = defaultdict(list)
        for n1, n2 in connections:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)

        self.cables = 0 # edges
        def dfs(node, visited, neighbors, parent):
            if (node in visited):
                self.cables += 1 # counted twice per connected
                return
            visited.add(node)
            for child in neighbors[node]:
                if child != parent: # not a loop
                    dfs(child, visited, neighbors, node)
        
        count = 0
        visited = set()
        for node in range(n):
            if node not in visited:
                count += 1 # count of disconnected computer
                dfs(node, visited, neighbors, -1)
        if(self.cables // 2 >= count - 1): # possible to connect all?
            return count - 1
        return -1
