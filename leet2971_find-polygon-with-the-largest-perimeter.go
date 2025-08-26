func largestPerimeter(nums []int) int64 {
    sort.Ints(nums)
    total := 0

    for _, v := range nums {
        total += v 
    }

    for i := len(nums) - 1; i >= 0; i-- {
        total -= nums[i]
        if total > nums[i] {
            return int64(total + nums[i])
        }
    }
    return -1
}