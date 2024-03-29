class MagicDictionary:

    def __init__(self):
        self.word_dict = {}
        

    def buildDict(self, dictionary: List[str]) -> None:
        for w in dictionary:
            self.word_dict[len(w)] = self.word_dict.get(len(w), []) + [w]

    def search(self, searchWord: str) -> bool:
        for candidate in self.word_dict.get(len(searchWord), []):
            countdiff = 0
            for i in range(len(searchWord)):
                if candidate[i] != searchWord[i]:
                    countdiff += 1
            if countdiff == 1:
                return True
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
