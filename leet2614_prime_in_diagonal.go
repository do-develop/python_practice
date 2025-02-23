func diagonalPrime(nums [][]int) int {
    largest := 0
    N := len(nums)

    for i := 0; i < N; i++ {
        if isPrime(nums[i][i]) {
            largest = int(math.Max(float64(largest), float64(nums[i][i])))
        }
        if isPrime(nums[i][N - i - 1]) {
            largest = int(math.Max(float64(largest), float64(nums[i][N - i - 1])))
        }
    }
    return largest
}

func isPrime(num int) bool {
    if num <= 1 {
        return false
    }
    if num <= 3 {
        return true
    }
    if num % 2 == 0 || num % 3 == 0 {
        return false
    }

    for i := 5; i * i <= num; i += 6 {
        if num % i == 0 || num % (i + 2) == 0{
            return false
        }
    }
    return true
}