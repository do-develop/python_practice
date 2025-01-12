func closestPrimes(left int, right int) []int {
    // Mark Non-Prime numbers (Sieve of Eratosthenes)
    seive := make([]bool, right + 1)
    for i := 2; i*i <= right; i++ {
        for j := 2; j*i <= right; j++ {
            if !seive[j * i] {
                seive[j * i] = true
            }
        }
    }

    prevPrime, x, y := -1, -1, -1
    if left == 1 {
        left = 2
    }
    for i := left; i <= right; i++ {
        if !seive[i] {
            if (prevPrime != -1) && (x != -1) && (y != -1) {
                if (i - prevPrime) < (y - x) {
                    x = prevPrime
                    y = i
                }
            } else {
                if prevPrime == -1 {
                    x = i
                } else if y == -1 {
                    y = i
                }
            }
            prevPrime = i
        }
    }
    if x == -1 || y == -1 {
        return []int{-1, -1}
    }
    return []int{x, y}
}