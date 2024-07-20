class Solution:
    def minimizeResult(self, expression: str) -> str:
        left, right = expression.split('+')
        score = float('inf')
        res = ''

        for i in range(len(left)):
            n1 = int(left[:i]) if i != 0 else 1
            n2 = int(left[i:])
            for j in range(1, len(right) + 1):
                n3 = int(right[:j])
                n4 = int(right[j:]) if j != len(right) else 1
                curr_score = n1 * (n2 + n3) * n4
                if curr_score < score:
                    score = curr_score
                    res = left[:i] + '(' + left[i:] + '+' + right[:j] + ')' + right[j:]
        return res
