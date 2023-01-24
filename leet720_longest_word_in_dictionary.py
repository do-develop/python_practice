class Solution:
    def longestWord(self, words: List[str]) -> str:
        longest = ""
        wordset = set(words)
        for word in words:
            if (len(word) > len(longest) or len(word) == len(longest) and word < longest):
                if all(word[:k] in wordset for k in range(1, len(word))):
                    longest = word
        return longest
