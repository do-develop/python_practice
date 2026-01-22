func nonSpecialCount(l int, r int) int {
    special, primes := 0, make([]bool, 31623)

    for i := 2; i * i <= r; i++ {
        primes[i] = isPrime(i)
    }

    for i := 2; i * i <= r; i++ {
        if !primes[i] {
            continue
        }
        if i * i >= l {
            special++
        }
    }

    return r - l + 1 - special
}

func isPrime(x int) bool {
    for i := 2; i * i <= x; i++ {
        if x % i == 0 {
            return false
        }
    }
    return true
}