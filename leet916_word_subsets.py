class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        target = {}
        for word in words2:
            counter = {}
            for c in word:
                if c not in counter:
                    counter[c] = 1
                else:
                    counter[c] += 1
            for c, cnt in counter.items():
                if c in target:
                    target[c] = max(cnt, target[c])
                else:
                    target[c] = cnt
        
        subsets = []
        for word in words1:
            for key in target:
                if word.count(key) < target[key]:
                    break
            else:
                subsets.append(word)
        return subsets
