func duplicateNumbersXOR(nums []int) int {
    repeated := make(map[int]bool)
    res := 0

    for _, num := range nums {
        if repeated[num] {
            res ^= num
        } else {
            repeated[num] = true
        }
    }
    return res
}