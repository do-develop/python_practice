class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        counter, res = {}, None
        for char in licensePlate:
            if char.isalpha():
                counter[char.lower()] = counter.get(char.lower(), 0) + 1
        
        for word in words:
            check = dict(counter)
            for c in word:
                if c.lower() in check:
                    check[c] -= 1
                    if not check[c]:
                        del check[c]
            if not check and (not res or len(word) < len(res)):
                res = word
        return res
