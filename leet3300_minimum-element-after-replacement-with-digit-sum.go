func minElement(nums []int) int {
    for i, n := range nums {
        nums[i] = 0
        for n > 0 {
            nums[i] += n % 10
            n /= 10
        }
    }
    sort.Ints(nums)
    return nums[0]
}