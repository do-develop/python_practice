class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        def is_prime(x):
            if x <= 1:
                return False
            if x <= 3:
                return True
            if x % 2 == 0 or x % 3 == 0:
                return False
            
            i = 5
            while i * i <= x:
                if x % i == 0 or x % (i + 2) == 0:
                    return False
                i += 6
            return True
        
        primes = set()
        N = len(s)

        for i in range(N):
            candidate = int(s[i])
            if is_prime(candidate):
                primes.add(candidate)
            for j in range(i + 1, N):
                candidate = candidate * 10 + int(s[j])
                if is_prime(candidate):
                    primes.add(candidate)
        
        return sum(sorted(primes, reverse=True)[:3])
