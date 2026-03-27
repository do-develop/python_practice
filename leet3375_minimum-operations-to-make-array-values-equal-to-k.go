func minOperations(nums []int, k int) int {
    setOfNum := make(map[int]bool)
    for _, x := range nums {
        if x < k {
            return -1
        } else if x > k {
            setOfNum[x] = true
        }
    }
    return len(setOfNum)
}