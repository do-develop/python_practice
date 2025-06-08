func maxSum(nums []int, m int, k int) int64 {
    N := len(nums)
    unique := map[int]int{}

    mxSum, currSum := int64(0), int64(0)

    for i := 0; i < N; i++ {
        num := nums[i]
        unique[num]++
        currSum += int64(num)

        if i >= k {
            unique[nums[i - k]]-- // remove left element
            if unique[nums[i - k]] == 0 {
                delete(unique, nums[i - k])
            }
            currSum -= int64(nums[i - k])
        }

        if i >= k - 1 && len(unique) >= m {
            mxSum = max(mxSum, currSum)
        }
    }
    return mxSum
}