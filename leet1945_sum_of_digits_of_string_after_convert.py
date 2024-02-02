class Solution:
    def getLucky(self, s: str, k: int) -> int:
        number = []
        for c in s:
            number.append(str(ord(c) - 96))
        s = ''.join(number)
        for _ in range(k):
            total = 0
            for c in s:
                total += int(c)
            s = str(total)
        return int(s)
