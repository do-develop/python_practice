class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        freq = [0] * 26
        for ch in word2:
            freq[ord(ch) - ord('a')] += 1
        
        windowFreq = [0] * 26
        result = left = count = 0

        for right in range(len(word1)):
            charIdx = ord(word1[right]) - ord('a')
            windowFreq[charIdx] += 1

            if windowFreq[charIdx] == freq[charIdx]:
                count += 1
            
            while count == sum(1 for cnt in freq if cnt > 0):
                result += len(word1) - right
            
                leftCharIdx = ord(word1[left]) - ord('a')
                if windowFreq[leftCharIdx] == freq[leftCharIdx]:
                    count -= 1
                
                windowFreq[leftCharIdx] -= 1
                left += 1
        return result
