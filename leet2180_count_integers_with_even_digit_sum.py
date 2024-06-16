class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for n in range(2, num+1):
            digits = list(str(n))
            total = 0
            for d in digits:
                total += int(d)
            if total % 2 == 0:
                count += 1
        return count
