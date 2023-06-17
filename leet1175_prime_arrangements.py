class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        # sieve of Eratosthenes
        primes = [True for _ in range(n + 1)]
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        prime_count = sum(primes[2:])
        return math.factorial(prime_count) * math.factorial(n - prime_count) % (10**9 + 7)
