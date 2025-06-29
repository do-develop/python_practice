func maximumTripletValue(nums []int) int64 {
    maxNum := 0   // max nums[i]
    maxDiff := 0  // max (nums[i] - nums[j])
    maxVal := 0   // max (nums[i] - nums[j]) * nums[k]

    for _, n := range nums {
        if maxDiff * n > maxVal {
            maxVal = maxDiff * n
        }

        if maxNum - n > maxDiff {
            maxDiff = maxNum - n
        }

        if n > maxNum {
            maxNum = n
        }
    }

    if maxVal < 0 {
        return 0
    }
    return int64(maxVal)
}