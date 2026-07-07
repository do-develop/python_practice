func maximumProduct(nums []int, m int) int64 {
    N := len(nums)
    maxi, mini := nums[0], nums[0]
    var res int64 = math.MinInt64

    for i := m - 1; i < N; i++ {
        idx := i - m + 1
        if nums[idx] > maxi {
            maxi = nums[idx]
        }
        if nums[idx] < mini {
            mini = nums[idx]
        }

        case1 := int64(mini) * int64(nums[i])
        case2 := int64(maxi) * int64(nums[i])

        if case1 > res {
            res = case1
        }
        if case2 > res {
            res = case2
        }
    }
    return res
}