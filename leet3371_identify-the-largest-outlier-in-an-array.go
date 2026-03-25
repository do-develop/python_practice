func getLargestOutlier(nums []int) int {
    freq := make(map[int]int)
    total := 0

    for _, n := range nums {
        freq[n]++
        total += n
    }

    ans := math.MinInt
    for _, n := range nums {
        freq[n]--
        if freq[n] == 0 {
            delete(freq, n)
        }

        curr := total - n
        if curr % 2 == 0 {
            if _, exists := freq[curr/2]; exists {
                if n > ans {
                    ans = n
                }
            }
        }
        freq[n]++
    }
    return ans
}