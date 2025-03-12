func distinctDifferenceArray(nums []int) []int {
    N := len(nums)
    res := make([]int, N)
    prefix, suffix := make(map[int]int), make(map[int]int)
    for i:= 0; i < N; i++ {
        suffix[nums[i]]++
    }

    for i :=0; i < N; i++ {
        prefix[nums[i]]++
        suffix[nums[i]]--

        if suffix[nums[i]] == 0 {
            delete(suffix, nums[i])
        }
        res[i] = len(prefix) - len(suffix)
    }
    return res
}
