class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counter1 = {}
        counter2 = {}

        for word in words1:
            counter1[word] = 1 if word not in counter1 else counter1[word] + 1

        for word in words2:
            counter2[word] = 1 if word not in counter2 else counter2[word] + 1
        
        set1 = set()
        set2 = set()
        for k, v in counter1.items():
            if v == 1:
                set1.add(k)
        for k, v in counter2.items():
            if v == 1:
                set2.add(k)
        
        return len(set1.intersection(set2))
