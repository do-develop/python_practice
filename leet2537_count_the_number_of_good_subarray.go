func countGood(nums []int, k int) int64 {
    var pairs int64 = 0
    var total int64 = 0
    seen := make(map[int]int)
    N := int64(len(nums))
    l := 0
    for r := 0; r < len(nums); r++ {
        seen[nums[r]]++
        pairs += int64(seen[nums[r]] - 1)
        for l < r && pairs > int64(k - 1) {
            pairs -= int64(seen[nums[l]] - 1)
            seen[nums[l]]--
            l++
        }
        total += int64(r - l + 1)
    }
    return N * (N + 1) / 2 - total
}