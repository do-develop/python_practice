class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        exist = True
        while exist:
            exist = False
            i = s.find(part)
            if i != -1:
                s = s[:i] + s[i + len(part):]
                exist = True
        return s
