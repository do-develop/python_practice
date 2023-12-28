class Solution:
    def minSwaps(self, s: str) -> int:
        def count_swap(ch):
            count = 0
            for c in s[::2]:
                if (c != ch):
                    count += 1
            return count

        c0, c1 = s.count('0'), s.count('1')

        if (c0 == c1):
            return min(count_swap('0'), count_swap('1'))
        if (c0 == c1 + 1):
            return count_swap('0')
        if (c0 + 1 == c1):
            return count_swap('1')
        return -1
