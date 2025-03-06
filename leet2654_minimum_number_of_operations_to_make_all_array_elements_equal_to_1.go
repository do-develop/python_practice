func minOperations(nums []int) int {
    N := len(nums)
    ones := 0
    for _, num := range(nums) {
        if num == 1 {
            ones++
        }
    }

    if ones > 0 {
        return N - ones
    }

    ops := math.MaxInt32
    for i := 0; i < N; i++ {
        num := nums[i]
        for j := i + 1; j < N; j++ {
            num = gcd(num, nums[j])
            if num == 1 {
                ops = min(ops, j - i)
                break
            }
        }
        
        if num != 1 {
            break
        }
    }
    if ops == math.MaxInt32 {
        return -1
    }
    return N - 1 + ops
}

func gcd(x, y int) int {
    if x == 0 {
        return y
    }
    return gcd(y % x, x)
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}
