class Solution:
    def checkString(self, s: str) -> bool:
        curr = s[0]

        if s[0] == 'b' and 'a' in s:
            return False
        
        N = len(s)
        for i in range(N):
            if curr == s[i]:
                continue
            elif curr in s[i+1:]:
                return False
        return True
