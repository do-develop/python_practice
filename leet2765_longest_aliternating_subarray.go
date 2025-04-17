func alternatingSubarray(nums []int) int {
    N := len(nums)
    if N < 2 {
        return -1
    }
    left := 0
    ans := -1
    if nums[0] + 1 == nums[1] {
        ans = 2
    }

    sign := 1
    for right := 1; right < N; right++ {
        prev := nums[right-1]
        curr := nums[right]

        if prev + sign != curr { // doesn't fit the expected alternating pattern
            // reset the left index
            if prev + 1 == curr {
                left = right - 1
            } else {
                left = right
            }
            if left == right {
                sign = 1
            } else {
                sign = -1
            }
        } else {
            if right - left + 1 > ans {
                ans = right - left + 1
            }
            sign *= -1
        }
    }
    return ans
}