# BFS approach
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        depth = -1
        visited, q = set(deadends), deque(['0000'])

        while q:
            size = len(q)
            depth += 1
            for _ in range(size):
                combi = q.popleft()
                if combi == target:
                    return depth
                if combi in visited:
                    continue
                visited.add(combi)
                q.extend(self.next_combination(combi))
        return -1

    def next_combination(self, combi):
        res = []
        for i, c in enumerate(combi):
            num = int(c)
            res.append(combi[:i] + str((num - 1) % 10) + combi[i+1:])
            res.append(combi[:i] + str((num + 1) % 10) + combi[i+1:])
        return res
