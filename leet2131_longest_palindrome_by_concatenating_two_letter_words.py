class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = defaultdict(lambda:0)
        for word in words:
            counter[word] += 1
        
        pair = palindrome = inmiddle = 0
        word_set = set(words)

        for word in word_set:
            if word == word[::-1]:
                if counter[word] % 2 == 1:
                    inmiddle = 1
                palindrome += (counter[word] // 2) * 2
            elif counter[word[::-1]] > 0:
                pair += 2 * min(counter[word], counter[word[::-1]])
                counter[word] = 0
        return (palindrome + inmiddle + pair) * 2 # two lowercase letters
