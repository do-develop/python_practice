class Solution:
    def rotatedDigits(self, n: int) -> int:
        s1 = set([1, 8, 0])
        s2 = set([1, 8, 0, 6, 9, 2, 5])
        def is_good(num):
            num_set = set([int(i) for i in str(num)])
            return num_set.issubset(s2) and not num_set.issubset(s1)
        return sum(is_good(i) for i in range(n + 1))
