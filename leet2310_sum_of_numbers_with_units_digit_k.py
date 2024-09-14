class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        for i in range(1, 11):
            # The sum of the integers is num
            # The units digit of each integer is k
            if k * i % 10 == num % 10 and i * k <= num:
                return i
        return -1
