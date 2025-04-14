func longestAlternatingSubarray(nums []int, threshold int) int {
    longest, i, N := 0, 0, len(nums)

    for i < N {
        // find the start point
        if nums[i] % 2 == 1 || nums[i] > threshold {
            i++
            continue
        }

        start := i
        for i < N - 1 && nums[i] % 2 != nums[i + 1] % 2 && nums[i + 1] <= threshold {
            i++
        }
        i++ // to include the last valid element (i + 1)
        longest = max(longest, i - start)
    }
    return longest
}

func max(x, y int) int {
    if x < y {
        return y
    }
    return x
}