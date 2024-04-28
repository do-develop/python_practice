class Solution:
    def countPoints(self, rings: str) -> int:
        count = 0
        R = [0] * 10
        G = [0] * 10
        B = [0] * 10
        N = len(rings)

        # store the position of the ring
        for i in range(0, N, 2):
            pos = ord(rings[i + 1]) - ord('0')
            if rings[i] == 'R':
                R[pos] += 1
            elif rings[i] == 'G':
                G[pos] += 1
            elif rings[i] == 'B':
                B[pos] += 1
            
        for i in range(0, 10):
            if R[i] > 0 and G[i] > 0 and B[i] > 0:
                count += 1
        return count
