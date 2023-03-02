class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # find m * p == n * q, where
        # m = number of room extension + 1
        # n = number of light extention + 1

        # if m even & n odd --> 0
        # if m odd & n odd --> 1
        # if m odd & n even --> 2

        m, n = q, p
        while (m % 2 == 0 and n % 2 == 0):
            m /= 2
            n /= 2
        
        if (m % 2 == 0 and n % 2 == 1): return 0
        if (m % 2 == 1 and n % 2 == 1): return 1
        if (m % 2 == 1 and n % 2 == 0): return 2
        return -1
