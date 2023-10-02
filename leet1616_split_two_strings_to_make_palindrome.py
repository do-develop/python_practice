class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        l, r = 0, len(a) - 1
        while l < r and a[l] == b[r]:
            l, r = l + 1, r - 1
        s1, s2 = a[l: r + 1], b[l: r + 1]

        l, r = 0, len(a) - 1
        while l < r and b[l] == a[r]:
            l, r = l + 1, r - 1
        s3, s4 = a[l: r + 1], b[l: r + 1]

        return any(s == s[::-1] for s in (s1, s2, s3, s4))
