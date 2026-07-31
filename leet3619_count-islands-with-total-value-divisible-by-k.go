func splitArray(nums []int) int64 {
    N := len(nums)

    sieve := make([]bool, N)
    sieve[0] = true
    if N > 1 {
        sieve[1] = true
    }

    for i := 2; i * i <= N; i++ {
        if !sieve[i] {
            for j := i * i; j < N; j += i {
                sieve[j] = true
            }
        }
    }

    sum1 := int64(0)
    sum2 := int64(0)

    for i := 0; i < N; i++ {
        if sieve[i] {
            sum1 += int64(nums[i])
        } else {
            sum2 += int64(nums[i])
        }        
    }
    return abs(sum1 - sum2)
}

func abs(x int64) int64 {
    if x < 0 {
        return -x
    }
    return x
}