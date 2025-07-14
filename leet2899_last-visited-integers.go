func lastVisitedIntegers(nums []int) []int {
    seen := make([]int, len(nums))
    var ans []int
    var pos, idx int = -1, -1
    
    for _, n := range nums {
        if n == -1 {
            if pos >= 0 {
                ans = append(ans, seen[pos])
                pos--
            } else {
                ans = append(ans, -1)
            }
        } else {
            idx++
            pos = idx
            seen[idx] = n
        }
    }
    return ans
}