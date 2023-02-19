class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def possible_decimal(s):
            res = set()
            if s[0]!='0' or len(s)==1:
                res.add(s)
            for i in range(1, len(s)):
                left, right = s[:i], s[i:]
                # left val is only one digit or the first digit is not 0
                if len(left)==1 or not left[0]=='0':
                    if right[-1] != '0': # and right most doesnt end with extra 0
                        res.add(left + '.' + right)
            return res
        # remove parenthesis
        s = s[1:-1]
        ans = []
        for i in range(1, len(s)):
            s1, s2 = s[:i], s[i:]
            s1, s2 = possible_decimal(s1), possible_decimal(s2)
            if not s1 or not s2:
                continue
            for c1 in s1:
                for c2 in s2:
                    ans.append('(' + c1 + ', ' + c2 + ')')
        return ans
