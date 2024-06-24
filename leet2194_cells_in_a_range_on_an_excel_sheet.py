from typing import List

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        x1, y1 = s[0], s[1]
        x2, y2 = s[3], s[4]
        ans = []

        for c in range(ord(x1), ord(x2) + 1):
            for r in range(int(y1), int(y2) + 1):
                ans.append(chr(c) + str(r))
        
        return ans
