func maximumSubarraySum(nums []int, k int) int64 {
    // sliding window approach
    N := len(nums)
    prevIdx := make(map[int]int) // num => last duplicate occuring index
    currSum := int64(0)
    maxSum := int64(0)
    begin := 0

    for end := 0; end < N; end++ {
        currSum += int64(nums[end])

        i, exist := prevIdx[nums[end]]
        if !exist {
            i = -1
        }
        
        for begin <= i || end - begin + 1 > k {
            currSum -= int64(nums[begin])
            begin++
        }

        if end - begin + 1 == k {
            if currSum > maxSum {
                maxSum = currSum
            }
        }

        prevIdx[nums[end]] = end
    }

    return maxSum
}