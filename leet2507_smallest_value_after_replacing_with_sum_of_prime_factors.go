func smallestValue(n int) int {
    // sortPrimes := make([]int, 0, 16)
    // primeMap := make(map[int]bool)

    // for i := 2; i <= n; i++ {
    //     if isPrime(i) {
    //         sortPrimes = append(sortPrimes, i)
    //         primeMap[i] = true
    //     }
    // }

    // for {
    //     next := primeSum(n, sortPrimes, primeMap)
    //     if next == n { // case of 4
    //         return next
    //     }
    //     n = next
    // }

    prev, total := n, 0
    for n % 2 == 0 {
        total += 2
        n /= 2
    }

    for i := 3; i <= n; i += 2 {
        for n % i == 0 {
            total += i
            n /= i
        }
    }

    if total != prev {
        return smallestValue(total)
    }
    return total
}

func isPrime(v int) bool {
    switch {
        case v == 2:
            return true
        case v % 2 == 0:
            return false
        default:
    }
    for i := 3; i*i <= v; i += 2 {
		if v%i == 0 {
			return false
		}
	}
	return true
}

func primeSum(n int, sortPrimes []int, primeMap map[int]bool) int {
    total := 0
    for n != 1 {
        if primeMap[n] {
            total += n
            return total
        }
        for i := 0; i < len(sortPrimes); {
            if n % sortPrimes[i] == 0 {
                n = n / sortPrimes[i]
                total += sortPrimes[i]
            } else {
                i++
            }
        }
    }
    return total
}