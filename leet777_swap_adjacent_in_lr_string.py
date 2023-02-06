class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # L, R orders must be the same
        if start.replace("X", "") != end.replace("X", ""):
            return False
        
        size = len(start)
        start_L = [i for i in range(size) if start[i] == 'L']
        end_L = [i for i in range(size) if end[i] == 'L']
        start_R = [i for i in range(size) if start[i] == 'R']
        end_R = [i for i in range(size) if end[i] == 'R']

        for s, e in zip(start_L, end_L):
            if s < e: # L can only move to the left
                return False
        
        for s, e in zip(start_R, end_R):
            if s > e: # R can only move to the right
                return False

        return True
