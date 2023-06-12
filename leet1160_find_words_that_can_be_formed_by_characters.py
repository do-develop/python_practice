class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total = 0
        chars_count = collections.Counter(chars)
        for word in words:
            word_count = collections.Counter(word)
            if all(chars_count[c] >= word_count[c] for c in word_count):
                total += len(word)
        return total
