class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        # operations in function
        def rotate(s, b):
            return s[len(s)-b: ] + s[:len(s)-b]
        
        def add(s, a):
            new = ""
            for i in range(len(s)):
                if i % 2 == 0:
                    new += s[i]
                else:
                    new += str(int(s[i]) + a)[-1]
            return new
        
        # perform search
        seen = set()
        need = list()
        need.append(s)

        while need:
            curr = need.pop()
            if curr not in seen:
                seen.add(curr)
                need.extend([add(curr, a), rotate(curr, b)])
        return min(seen)
