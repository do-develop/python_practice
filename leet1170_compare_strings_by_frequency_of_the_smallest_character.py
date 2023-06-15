class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            smallest = sorted(list(s))[0]
            return s.count(smallest)
        
        query = [f(x) for x in queries]
        word = [f(x) for x in words]
        res = []
        for x in query:
            count = 0
            for y in word:
                if y > x:
                    count += 1
            res.append(count)
        return res
