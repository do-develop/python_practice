class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        count_top = defaultdict(int)
        count_bot = defaultdict(int)
        same = 0
        N = len(tops)

        for i in range(N):
            count_top[tops[i]] += 1
            count_bot[bottoms[i]] += 1
            if tops[i] == bottoms[i]:
                same += 1
        
        for x in range(1, 7):
            if (count_top[x] + count_bot[x] - same) == N:
                return N - max(count_top[x], count_bot[x])
        return -1
