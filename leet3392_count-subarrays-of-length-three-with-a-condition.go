func countSubarrays(nums []int) int {
    N := len(nums)
    ans := 0
    for i := 1; i < N - 1; i++ {
        if nums[i] == (nums[i-1] + nums[i+1]) * 2 {
            ans++
        }
    }
    return ans
}