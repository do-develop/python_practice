func findTheArrayConcVal(nums []int) int64 {
    N := len(nums)
    l, r := 0, N - 1
    total := 0

    for l <= r {
        if l == r {
            total += nums[l]
        } else {
            digits := strconv.Itoa(nums[l]) + strconv.Itoa(nums[r])
            value, _ := strconv.Atoi(digits)
            total += value
        }
        l++
        r--
    }
    return int64(total)
}