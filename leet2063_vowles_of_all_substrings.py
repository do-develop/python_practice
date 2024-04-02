class Solution:
    def countVowels(self, word: str) -> int:
        N = len(word)
        count = 0
        for i, c in enumerate(word):
            if c in 'aeiou':
                count += (i + 1) * (N - i)
        return count
