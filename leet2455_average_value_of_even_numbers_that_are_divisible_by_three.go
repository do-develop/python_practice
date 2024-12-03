func averageValue(nums []int) int {
    total, count := 0, 0

    for i := range nums {
        if nums[i] % 6 == 0 {
            total += nums[i]
            count++
        }
    }
    if count > 0 {
        return total / count
    }
    return 0
}