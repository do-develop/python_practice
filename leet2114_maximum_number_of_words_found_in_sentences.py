class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        most = 0

        for sentence in sentences:
            words = sentence.split()
            most = max(most, len(words))
        return most
