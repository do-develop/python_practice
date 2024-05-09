class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        N = len(s)
        ans = [0] * N

        for i in range(N):
            cnt = 0
            x, y = startPos
            
            for c in s[i:]:
                if c == "U":
                    x -= 1
                elif c == "D":
                    x += 1
                elif c == "R":
                    y += 1
                else:
                    y -= 1
            
                if x < 0 or y < 0 or x >= n or y >= n:
                    break
                cnt += 1
                
            ans[i] = cnt
        return ans
