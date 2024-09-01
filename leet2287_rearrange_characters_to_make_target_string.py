class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        cnt_target = Counter(target)
        cnt_s = Counter(s)
        ans = 10000

        for i in cnt_target:
            ans = min(ans, cnt_s[i] // cnt_target[i])
        return ans
