func minimumOperations(nums []int) int {
    ops := 0
    for i := 0; i < len(nums); i += 3{
        if hasAllUnique(nums, i) {
            return ops
        }
        ops++
    }
    return ops
}

func hasAllUnique(nums[] int, start int) bool {
    seen := make(map[int]bool)

    for _, num := range nums[start:] {
        if seen[num] {
            return false
        }
        seen[num] = true
    }
    return true
}