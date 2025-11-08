func maximumPrimeDifference(nums []int) int {
    primes := []int{}

    for i, n := range nums {
        if isPrime(n) {
            primes = append(primes, i)
        }
    }
    return primes[len(primes) - 1] - primes[0]
}

func isPrime(n int) bool {
    if n == 1 {
        return false
    }

    for i := 2; i <= int(math.Sqrt(float64(n) + 1)); i++ {
        if n % i == 0 {
            return false
        }
    }
    return true
}