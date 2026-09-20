func longestSubarray(nums []int) int {
    curr, longest := 2, 2

    for i := 2; i < len(nums); i++ {
        if nums[i] == nums[i-1] + nums[i-2] {
            curr++
            if curr > longest {
                longest = curr
            }
        } else {
            curr = 2
        }
    }
    return longest
}