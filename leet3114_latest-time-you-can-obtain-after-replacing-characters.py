class Solution:
    def findLatestTime(self, s: str) -> str:
        h1, h2, _, m1, m2 = list(s)

        if h1 == '?': h1 = '1' if h2 in '?01' else '0'
        if h2 == '?': h2 = '9' if h1 == '0' else '1'
        if m1 == '?': m1 = '5'
        if m2 == '?': m2 = '9'

        return h1 + h2 + ':' + m1 + m2
