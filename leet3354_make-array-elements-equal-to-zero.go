func countValidSelections(nums []int) int {
    count, nonZeros, N := 0, 0, len(nums)
    for _, n := range nums {
        if n > 0 {
            nonZeros++
        }
    }

    for i:=0; i < N; i++ {
        if nums[i] == 0 {
            if isValid(nums, nonZeros, i, -1) {
                count++
            }
            if isValid(nums, nonZeros, i, 1) {
                count++
            }
        }
    }
    return count
}

func isValid(nums []int, nonZeros, start, direction int) bool {
    temp := make([]int, len(nums))
    copy(temp, nums)
    curr := start

    for nonZeros > 0 && curr >= 0 && curr < len(nums) {
        if temp[curr] > 0 {
            temp[curr]--
            direction *= -1
            if temp[curr] == 0 {
                nonZeros--
            }
        }
        curr += direction
    }
    return nonZeros == 0
}