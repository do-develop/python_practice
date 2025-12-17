func minimumAverage(nums []int) float64 {
    sort.Ints(nums)
    averages := make([]float64, len(nums) / 2)
    l, r := 0, len(nums) - 1

    for l < r {
        averages[l] = float64(nums[l] + nums[r]) / 2
        l++
        r--
    }

    sort.Float64s(averages)
    return averages[0]
}