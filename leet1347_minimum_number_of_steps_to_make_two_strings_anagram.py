class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dic = collections.defaultdict(int)

        for char in s:
            dic[char] += 1
        for char in t:
            if dic[char]:
                dic[char] -= 1
        
        return sum(dic.values())
