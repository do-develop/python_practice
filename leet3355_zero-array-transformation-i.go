func isZeroArray(nums []int, queries [][]int) bool {
    operations := make([]int, len(nums) + 1)
    for _, query := range queries {
        left := query[0]
        right := query[1]
        operations[left] += 1
        operations[right + 1] -= 1
    }
    opsCount := make([]int, len(operations))
    currOps := 0

    for i, ops := range operations {
        currOps += ops
        opsCount[i] = currOps
    }

    for i := 0; i < len(nums); i++ {
        if opsCount[i] < nums[i] {
            return false
        }
    }
    return true
}