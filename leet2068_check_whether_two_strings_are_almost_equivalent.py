class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        counter = [0 for _ in range(26)]

        for i in range(len(word1)):
            counter[ord(word1[i]) - ord('a')] += 1
            counter[ord(word2[i]) - ord('a')] -= 1
        
        for i in range(26):
            if abs(counter[i]) > 3:
                return False
        return True
