class Solution:
    def longestBalanced(self, s: str) -> int:
        N = len(s)
        P = [[0,0,0]]
        for c in s:
            P.append(P[-1][:])
            P[-1]["abc".index(c)] += 1

        ans = 0
        first = {}
        for i , (a, b, c) in enumerate(P):
            for key in [
                ("abc", a - b, a - c),
                ("ab", a - b, c),
                ("bc", b - c, a),
                ("ca", c - a, b),
                ("a", b, c),
                ("b", c, a),
                ("c", a, b),
            ]:
                ans = max(ans, i - first.get(key, i))
                # the earliest prefix index with that key
                # records i only the first time the key appears
                first.setdefault(key, i)

        return ans