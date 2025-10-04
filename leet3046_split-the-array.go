func isPossibleToSplit(nums []int) bool {
    N := len(nums)
    arr := make([]int, 101)
    for i := 0; i < N; i++ {
        arr[nums[i]]++
        if arr[nums[i]] > 2 {
            return false
        }
    }
    return true
}