func longestSubsequence(nums []int) int {
    N := len(nums)
    totalXor := 0
    allZero := true

    for _, x := range nums {
        totalXor ^= x
        if x > 0 {
            allZero = false
        }
    }

    if totalXor > 0 {
        return N
    }

    if allZero {
        return 0
    }

    return N - 1
}