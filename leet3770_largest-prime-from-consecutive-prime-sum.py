class Solution:
    def largestPrime(self, n: int) -> int:
        # Sieve of Eratosthenes
        isPrime = [True] * (n + 1)
        if n >= 0:
            isPrime[0] = False
        if n >= 1:
            isPrime[1] = False

        for i in range(2, int(n**0.5) + 1):
            if isPrime[i]:
                for j in range (i * i, n + 1, i):
                    isPrime[j] = False
        

        primes = [i for i in range(2, n + 1) if isPrime[i]]

        # Find largest prime that is a sum of consecutive primes
        curr = res = 0

        for p in primes:
            curr += p
            if curr > n:
                break
            if isPrime[curr]:
                res = curr
        return res