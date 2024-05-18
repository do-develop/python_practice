class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        counter = {}
        for word in startWords:
            sorted_word = []
            for c in word:
                sorted_word.append(c)
            sorted_word.sort()
            counter[tuple(sorted_word)] = 1
        
        word_count = 0
        for word in targetWords:
            sorted_word = []
            for c in word:
                sorted_word.append(c)
            sorted_word.sort()
            sorted_tuple = tuple(sorted_word)
            for i in range(len(sorted_tuple)):
                if counter.get(sorted_tuple[:i] + sorted_tuple[i+1:]):
                    word_count += 1
                    break
        return word_count
