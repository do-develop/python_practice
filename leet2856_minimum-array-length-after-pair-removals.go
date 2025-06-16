func minLengthAfterRemovals(nums []int) int {
    N := len(nums)
    mid := N / 2

    right := N - 1
    left := mid - 1
    removals := 0

    for left >= 0 {
        if nums[right] > nums[left] {
            removals += 2
            right--
        }
        left--
    }

    return N - removals
}