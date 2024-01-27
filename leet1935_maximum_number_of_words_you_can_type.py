class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(' ')
        count = 0
        
        for word in words:
            cantype = True
            for c in brokenLetters:
                if c in word:
                    cantype = False
                    break
            if cantype:
                count += 1

        return count
