class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        pos = 0

        for word in words:
            if s[pos:pos + len(word)] != word:
                return False
            pos += len(word)
            if pos == len(s):
                return True
        return False
