class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False

        perimeter = sum(matchsticks)
        equal_side = perimeter // 4
        
        # if not equally divisible
        if equal_side * 4 != perimeter:
            return False
        
        matchsticks.sort(reverse=True)
        sides = [0 for _ in range(4)]
        
        def dfs(idx):
            if idx == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == equal_side
            
            for i in range(4):
                if sides[i] + matchsticks[idx] <= equal_side:
                    sides[i] += matchsticks[idx]
                    if dfs(idx + 1):
                        return True
                    sides[i] -= matchsticks[idx]
            return False
        
        return dfs(0)
