class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # linear scan approach
        # All the scores come from substring contain only a and b. 
        # So once we scan a character that is not one of them, we reset the scoring (a = b = 0).
        # Suppose x > y, then we should pair as much ab as possible. After that, we pair the ba from the rest a and b
        if x < y:
            x, y, s = y, x, s[::-1]
        a = b = ans = 0
        for c in s:
            if c == 'a':
                a += 1
            elif c == 'b':
                if a:
                    ans += x
                    a -= 1
                else:
                    b += 1
            else:
                ans += min(a,b)*y
                a = b = 0
        return ans + min(a,b)*y
