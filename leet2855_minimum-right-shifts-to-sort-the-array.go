func minimumRightShifts(nums []int) int {
    N := len(nums)
    broken := 0 // if broken more than once return -1


    if nums[N - 1] >= nums[0] {
        broken = N // No break found yet
    }

    for i := N - 1; i > 0; i-- {
        if (nums[i] < nums[i - 1]) {
            if broken != 0 {
                return -1
            }
            broken = i
        }
    } 
    return N - broken
}