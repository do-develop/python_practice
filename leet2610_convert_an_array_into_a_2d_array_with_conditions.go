func findMatrix(nums []int) [][]int {
    freq := make(map[int]int)
    ans  := make([][]int, 0)

    for _, val := range nums {
        if freq[val] >= len(ans) {
            ans = append(ans, []int{})
        }

        ans[freq[val]] = append(ans[freq[val]], val)
        freq[val]++
    }
    return ans
}