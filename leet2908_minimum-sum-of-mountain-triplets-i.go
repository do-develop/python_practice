func minimumSum(nums []int) int {
    minSum := math.MaxInt32
    N := len(nums)

    minLeft := make([]int, N)
    minRight := make([]int, N)

    minLeft[0] = math.MaxInt32
    for i := 1; i < N; i++ {
        minLeft[i] = min(nums[i - 1], minLeft[i - 1])
    }

    minRight[N-1] = math.MaxInt32
    for i := N - 2; i >= 0; i-- {
        minRight[i] = min(nums[i + 1], minRight[i + 1])
    }

    for i := 1; i < N - 1; i++ {
        if minLeft[i] < nums[i] && nums[i] > minRight[i] {
            minSum = min(minSum, minLeft[i] + nums[i] + minRight[i])
        }
    }

    if minSum != math.MaxInt32 {
        return minSum
    }
    return -1
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}