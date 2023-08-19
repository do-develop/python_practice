class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # 1 << k is the same as 2^k
        need = 1 << k
        have = set()

        for i in range(k, len(s) + 1):
            sub = s[i-k:i]
            if sub not in have:
                have.add(sub)
                need -= 1
                if need == 0:
                    return True
        return False
