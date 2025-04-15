func findPrimePairs(n int) [][]int {
    pairs := [][]int{}
    sieve := make([]bool, n + 1)

    // seive of Eratosthenes (mark non prime number)
    for p := 2; p * p < n; p++ {
        if !sieve[p] {
            for i := p * p; i < n; i += p {
                sieve[i] = true
            }
        }
    }
    for p := 2; p < n; p++ {
        if !sieve[p] && !sieve[n-p] && p <= n - p {
            pairs = append(pairs, []int{p, n-p})
        }
    }
    return pairs
}