func maximumMedianSum(nums []int) int64 {
    sort.Ints(nums)
    var medianSum int64

    for i, j := len(nums)-2, 0; j < len(nums)/3; i, j = i-2, j+1 {
        medianSum += int64(nums[i])
    }
    return medianSum
}