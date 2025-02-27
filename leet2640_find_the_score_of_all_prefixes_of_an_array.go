func findPrefixScore(nums []int) []int64 {
    prefix := []int64{}
    max := -1
    prev := 0

    for _, n := range nums {
        if max < n {
            max = n
        }

        val := n + max
        val += prev
        prefix = append(prefix, int64(val))
        prev = val
    }
    return prefix
}