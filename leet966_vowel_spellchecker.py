class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # three cases to check
        # 1 exact match
        # 2 capitalization
        # 3 vowel

        words_exact = set(wordlist)
        words_cap = {}
        words_vow = {}

        def vowel_replace(word):
            return "".join('*' if c in 'aeiou' else c for c in word.lower())

        for word in wordlist:
            wordlow = word.lower()
            words_cap.setdefault(wordlow, word)
            words_vow.setdefault(vowel_replace(wordlow), word)
        
        def solve(query):
            if query in words_exact: 
                return query
            lower = query.lower()
            if lower in words_cap: 
                return words_cap[lower]
            masked = vowel_replace(query)
            if masked in words_vow:
                return words_vow[masked]
            return ""
        
        return [solve(q) for q in queries]
        
