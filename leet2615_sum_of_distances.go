func distance(nums []int) []int64 {
    // Use prefix sum to improve performance
    N := len(nums)
    count := make(map[int][]int)
    ans := make([]int64, N)

    for i, num := range nums {
        count[num] = append(count[num], i)
    }

    for _, indices := range count {
        size := len(indices)
        if size == 1 {
            ans[indices[0]] = 0
        } else {
            var nextSum int64
            for _, i := range indices {
                nextSum += int64(i)
            }
            var prevSum int64
            for i := 0; i < size; i++ {
                idx := indices[i]
                tmp := nextSum - int64((size - i) * idx)
                tmp += int64(math.Abs(float64(prevSum - int64(i * idx))))
                ans[idx] = tmp
                nextSum -= int64(idx)
                prevSum += int64(idx)
            }
        }
    }
    return ans
}