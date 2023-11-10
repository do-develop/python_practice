class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        counter = dict()
        for i in range(lowLimit, highLimit + 1):
            digits = str(i)
            sum_of_digits = 0
            for digit in digits:
                sum_of_digits += int(digit)
            if sum_of_digits in counter:
                counter[sum_of_digits] += 1
            else:
                counter[sum_of_digits] = 1
        return max(counter.values())
