class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def numeric_pattern(w):
            word = []
            dic = defaultdict(int)
            i = 0
            for c in w:
                if c in dic:
                    word.append(dic[c])
                else:
                    i += 1
                    dic[c] = i
                    word.append(dic[c])
            return word
        
        ans = []
        pattern_p = numeric_pattern(pattern)
        for w in words:
            word_p = numeric_pattern(w)
            if word_p == pattern_p: ans.append(w)
        return ans
