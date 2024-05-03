class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        words = []
        start = 0

        for i in range(len(spaces)):
            words.append(s[start:spaces[i]])
            start = spaces[i]
        words.append(s[start:])
        return ' '.join(words)
