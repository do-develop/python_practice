func minimumSumSubarray(nums []int, l int, r int) int {
    mini := math.MaxInt32

    for w := l; w <= r; w++ {
        left, temp := 0, 0
        for right := 0; right < len(nums); right++ {
            if right - left + 1 <= w {
                temp += nums[right]

                if right - left + 1 == w {
                    if temp > 0 {
                        mini = min(mini, temp)
                    }
                    temp -= nums[left]
                    left++
                }
            }
        }
    }
    if mini == math.MaxInt32 { return -1 }
    return mini
}