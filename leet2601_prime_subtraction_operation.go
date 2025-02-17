func primeSubOperation(nums []int) bool {
    maxElement := 0
    for _, num := range nums {
        if num > maxElement {
            maxElement = num
        }
    }

    previousPrime := make([]int, maxElement + 1)
    for i := 2; i <= maxElement; i++ {
        if isPrime(i){
            previousPrime[i] = i
        } else {
            previousPrime[i] = previousPrime[i - 1]
        }
    }

    for i := 0; i < len(nums); i++ {
        var bound int
        if i == 0 {
            bound = nums[0]
        } else {
            bound = nums[i] - nums[i - 1]
        }

        if bound <= 0 {
            return false
        }
        largestPrime := previousPrime[bound - 1]
        nums[i] -= largestPrime
    }
    return true
}

func isPrime(n int) bool {
    if n < 2 {
        return false
    }
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n % i == 0 {
            return false
        }
    }
    return true
}

