func missingMultiple(nums []int, k int) int {
    seen := make(map[int]bool)

    for _, num := range nums {
        seen[num] = true
    }

    multi := k 
    for seen[multi] {
        multi += k
    }
    return multi
}