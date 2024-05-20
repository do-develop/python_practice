class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        
        for i in range(0, len(s), k):
            word = s[i: i + k]
            if len(word) == k:
                res.append(word)
            else:
                fill_count = k - len(word)
                for _ in range(fill_count):
                    word += fill
                res.append(word)
        return res
