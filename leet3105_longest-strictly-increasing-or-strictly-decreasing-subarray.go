func longestMonotonicSubarray(nums []int) int {
    if len(nums) == 1 {
        return 1
    }

    longest := 0
    asc, des := 1, 1

    for i := 0; i < len(nums) - 1; i++ {
        if nums[i] > nums[i + 1] {
            des++
            asc = 1
        } else if nums[i] < nums[i + 1] {
            asc++
            des = 1
        } else {
            asc = 1
            des = 1
        }
        longest = max(longest, max(asc, des))
    }
    return longest
}