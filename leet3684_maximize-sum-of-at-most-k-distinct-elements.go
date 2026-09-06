func maxKDistinct(nums []int, k int) []int {
    sort.Ints(nums)
    N := len(nums)
    res := make([]int, 1, k)
    res[0] = nums[N - 1]

    for i := N - 2; i >= 0; i-- {
        if k > 1 && nums[i] != nums[i+1] {
            res = append(res, nums[i])
            k--
        }
    }
    return res
}