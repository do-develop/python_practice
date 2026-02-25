class Solution:
    def _isVowel(self, c: str) -> bool:
        return c == "a" or c == "e" or c == "i" or c == "o" or c == "u"

    def countOfSubstrings(self, word: str, k: int) -> int:
        valid_count = 0
        start = end = 0
        vowels = {}
        consonant_count = 0
        # precompute next consonant position
        next_consonant = [0] * len(word)
        next_consonant_index = len(word)

        for i in range(len(word) - 1, -1, -1):
            next_consonant[i] = next_consonant_index
            if not self._isVowel(word[i]):
                next_consonant_index = i
            
        while end < len(word):
            new_c = word[end]
            if self._isVowel(new_c):
                vowels[new_c] = vowels.get(new_c, 0) + 1
            else:
                consonant_count += 1
            
            while consonant_count > k:
                start_c = word[start]
                if self._isVowel(start_c):
                    vowels[start_c] -= 1
                    if vowels[start_c] == 0:
                        del vowels[start_c]
                else:
                    consonant_count -= 1
                start += 1
            
            while start < len(word) and len(vowels) == 5 and consonant_count == k:
                valid_count += next_consonant[end] - end
                start_c = word[start]
                if self._isVowel(start_c):
                    vowels[start_c] -= 1
                    if vowels[start_c] == 0:
                        del vowels[start_c]
                else:
                    consonant_count -= 1
                start += 1

            end += 1
            
        return valid_count
