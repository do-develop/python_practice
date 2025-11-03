func minOperationsToMakeMedianK(nums []int, k int) int64 {
    slices.Sort(nums)
    midx := len(nums) / 2
    ops := 0

    for i, n := range nums {
        switch {
            case i <= midx && n > k:
                ops += (n - k)
            case i >= midx && n < k:
                ops += (k - n)
        }
    }
    return int64(ops)
}