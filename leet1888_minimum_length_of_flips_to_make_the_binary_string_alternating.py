class Solution:
    def minFlips(self, s: str) -> int:
        min_flips = len(s)
        window = len(s)
        # type-1 operation will have no effect on minimizing the flips if the string is of even length.
        s = s if window % 2 == 0 else s + s

        arr1, arr2 = [], []
        for i in range(len(s)):
            arr1.append('0' if i % 2 == 0 else '1')
            arr2.append('1' if i % 2 == 0 else '0')
    
        alternate1 = ''.join(arr1)
        alternate2 = ''.join(arr2)

        diff1, diff2 = 0, 0
        l, r = 0, 0
        while r < len(s):
            if s[r] != alternate1[r]: diff1 += 1
            if s[r] != alternate2[r]: diff2 += 1

            if r - l + 1 < window:
                r += 1
            else:
                min_flips = min(min_flips, diff1, diff2)
                if s[l] != alternate1[l]: diff1 -= 1
                if s[l] != alternate2[l]: diff2 -= 1
                l += 1
                r += 1
        return min_flips
