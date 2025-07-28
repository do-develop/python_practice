func minIncrementOperations(nums []int, k int) int64 {
    // sliding window approach
    N := len(nums)
    var ans int64 = 0

    for i := 1; i < N - 1; i++ {
        currMax := max(nums[i - 1], nums[i], nums[i + 1])

        if currMax < k {
            need := k - currMax
            // need to increment all three to make the max at least k
            nums[i - 1] += need
            nums[i]     += need
            nums[i + 1] += need
            // accumulate the cost of operation
            ans += int64(need)
        }
    }
    return ans
}

func max(a, b, c int) int {
    if a > b {
        if a > c {
            return a
        }
        return c
    } else {
        if b > c {
            return b
        }
        return c
    }
}