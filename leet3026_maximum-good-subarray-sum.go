func maximumSubarraySum(nums []int, k int) int64 {
    N := len(nums)
    prefixSum := make(map[int]int, N + 1)
    
    for i, num := range nums {
        prefixSum[i + 1] = prefixSum[i] + num
    }

    visited := make(map[int]int) // to track last seen indices
    var res int64 = math.MinInt64

    for i, num := range nums {
        if j, ok := visited[num]; ok && prefixSum[i] - prefixSum[j] < 0 {
            visited[num] = i
        } else if !ok {
            visited[num] = i
        }

        if j, ok := visited[num-k]; ok {
            res = max(res, int64(prefixSum[i+1]-prefixSum[j]))
        }

        if j, ok := visited[num+k]; ok {
            res = max(res, int64(prefixSum[i+1]-prefixSum[j]))
        }
    }

    if res == math.MinInt64 {
        return 0
    }

    return res
}