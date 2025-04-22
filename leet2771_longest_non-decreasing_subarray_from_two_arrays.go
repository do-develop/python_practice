func maxNonDecreasingLength(nums1 []int, nums2 []int) int {
    N := len(nums1)
    dp1 := make([]int, N)
    dp2 := make([]int, N)
    dp1[0] = 1
    dp2[0] = 1

    for i:= 1; i < N; i++ {
        dp1[i] = 1
        dp2[i] = 1

        if nums1[i] >= nums1[i - 1] {
            dp1[i] = max(dp1[i - 1] + 1, dp1[i])
        }
        if nums1[i] >= nums2[i - 1] {
            dp1[i] = max(dp2[i - 1] + 1, dp1[i])
        }
        if nums2[i] >= nums1[i - 1] {
            dp2[i] = max(dp1[i - 1] + 1, dp2[i])
        }
        if nums2[i] >= nums2[i - 1] {
            dp2[i] = max(dp2[i - 1] + 1, dp2[i])
        }
    }
    return max(max(dp1...), max(dp2...))
}

func max(values ...int) int {
    maxVal := math.MinInt64
    for _, v := range values {
        if v > maxVal {
            maxVal = v
        }
    }
    return maxVal
}