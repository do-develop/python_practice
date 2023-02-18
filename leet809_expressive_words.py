class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def compress(s):
            compressed = []
            count = 0
            prev_char = s[0]
            for c in s:
                if c == prev_char:
                    count += 1
                else:
                    compressed.append((prev_char, count))
                    count = 1
                prev_char = c
            compressed.append((prev_char, count))
            return compressed

        def check(word, comp_s):
            comp_word = compress(word)
            if len(comp_word) != len(comp_s):
                return False
            for i in range(len(comp_word)):
                if comp_s[i][0] != comp_word[i][0]:
                    return False
                if not (comp_s[i][1] == comp_word[i][1] or comp_s[i][1] >= max(3, comp_word[i][1])):
                    return False
            return True
        
        comp_s = compress(s)
        ans = 0
        for word in words:
            if check(word, comp_s):
                ans += 1
        return ans
