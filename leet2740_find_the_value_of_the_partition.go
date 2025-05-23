func findValueOfPartition(nums []int) int {
    sort.Ints(nums)
    res := math.MaxInt

    for i := 1; i < len(nums); i++ {
        res = min(res, nums[i] - nums[i-1])
    }
    return res
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}
