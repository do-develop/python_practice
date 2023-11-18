class Solution:
    def countHomogenous(self, s: str) -> int:
        total = curr = 0
        modulo = 10 ** 9 + 7

        for i in range(len(s)):
            if i == 0 or s[i] == s[i - 1]:
                curr += 1
            else:
                curr = 1
            total = (total + curr) % modulo
        return total
