class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # time = dist / speed
        N = len(dist)
        time = []
        for i in range(N):
            time.append(dist[i] / speed[i])
        time.sort()
        for i in range(N):
            if i >= time[i]:
                i -= 1
                break
        return i + 1
