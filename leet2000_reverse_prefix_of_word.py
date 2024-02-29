class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        
        word = list(word)
        idx = word.index(ch)
        reversed_part = word[:idx+1][::-1]
        word[:idx+1] = reversed_part
        return ''.join(word)
