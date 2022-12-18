class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))
        for word in dictionary:
            idx = 0
            for c in s:
                if idx < len(word) and word[idx] == c:
                    idx += 1
            if idx == len(word):
                return word
        return ""