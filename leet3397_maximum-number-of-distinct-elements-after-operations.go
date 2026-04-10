func maxDistinctElements(nums []int, k int) int {
    sort.Ints(nums)
    count := 0
    prev := math.MinInt32

    for _, num := range nums {
        curr := min(max(num - k, prev + 1), num + k)
        if curr > prev {
            count++
            prev = curr
        }
    }
    return count
}