class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        res = []
        len_low = len(str(low))
        len_high = len(str(high))

        for window in range(len_low, len_high + 1):
            for i in range(0, 10 - window):
                num = int(digits[i: i + window])
                if low <= num <= high:
                    res.append(num)
        return res
