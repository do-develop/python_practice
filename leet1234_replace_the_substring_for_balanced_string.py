class Solution:
    def balancedString(self, s: str) -> int:
        counter = collections.Counter(s)
        change = s_size = len(s)
        left = 0
        for right, c in enumerate(s):
            counter[c] -= 1
            while left < s_size and all(s_size / 4 >= counter[c] for c in 'QWER'):
                change = min(change, right - left + 1)
                counter[s[left]] += 1
                left += 1
        return change
