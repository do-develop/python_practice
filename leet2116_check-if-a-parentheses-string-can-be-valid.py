class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        N = len(s)
        if N % 2 != 0:
            return False

        def validate(s: str, locked: str, open: str) -> bool:
            balance, wild = 0, 0
            for i in range(N):
                if locked[i] == '1':
                    balance += 1 if s[i] == open else -1
                else:
                    wild += 1
                if wild + balance < 0:
                    return False
            return balance <= wild
        return validate(s, locked, '(') and validate(s[::-1], locked[::-1], ')')
