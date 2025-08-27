func numberGame(nums []int) []int {
    sort.Ints(nums)
    res :=  []int{}
    for i := 0; i < len(nums); i += 2 {
        x := nums[i]
        y := nums[i+1]
        res = append(res, y)
        res = append(res, x)
    }
    return res
}