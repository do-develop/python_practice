func divideArray(nums []int, k int) [][]int {
    sort.Ints(nums)
    var ans [][]int
    for i := 0; i< len(nums); i += 3 {
        a, b, c := nums[i], nums[i + 1], nums[i + 2]

        if c - a > k {
            return [][]int{}
        }
        ans = append(ans, []int{a, b, c})
    }
    return ans
}