class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c = r = o = a = count = 0
        for ch in croakOfFrogs:
            if ch == 'c':
                c += 1
            elif ch == 'r':
                r += 1
                if c < r: return -1
            elif ch == "o":
                o += 1
                if r < o: return -1
            elif ch == "a":
                a += 1
                if o < a: return -1
            elif ch =='k':
                count = max(count, c)
                c -= 1
                r -= 1
                o -= 1
                a -= 1
        return count if (c == 0 and r == 0 and o == 0 and a == 0) else -1
