class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # calculate force
        N = len(dominoes)
        force = [0] * N

        # force from left to right
        f = 0
        for i in range(N):
            if dominoes[i] == 'L':
                f = 0
            elif dominoes[i] == 'R':
                f = N
            else: # '.'
                f = max(f-1, 0) # previous force - 1 vs no force
            force[i] += f

        # force from right to left
        f = 0
        for i in range(N-1, -1, -1):
            if dominoes[i] == 'L':
                f = N
            elif dominoes[i] == 'R':
                f = 0
            else:
                f = max(f-1, 0)
            force[i] -= f
        
        return ''.join('.' if f == 0 else 'R' if f > 0 else 'L' for f in force)
