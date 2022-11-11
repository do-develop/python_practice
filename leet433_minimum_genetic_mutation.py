class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # BFS approach
        q = deque([(startGene, 0)])
        seen = {startGene}
        
        while q:
            node, count = q.popleft()
            if node == endGene:
                return count
            
            for c in "ACGT":
                for i in range(len(node)):
                    neighbor = node[:i] + c + node[i+1:]
                    if neighbor not in seen and neighbor in bank:
                        seen.add(neighbor)
                        q.append((neighbor, count + 1))
        return -1
            
