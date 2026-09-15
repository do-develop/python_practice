func splitArray(nums []int) int64 {
    N := len(nums)
    leftSum := int64(nums[0])
    i := 1
    for ; i < N && nums[i] > nums[i-1]; i++ {
        leftSum += int64(nums[i])
    }

    // if the array is strictly increasing
    if i == N {
        return abs(leftSum - int64(nums[i-1])*2)
    }

    rightSum := int64(nums[i])
    j := i + 1
    for ; j < N && nums[j] < nums[j-1]; j++ {
        rightSum += int64(nums[j])
    }

    // if the right subarray is not strictly decreasing
    if j < N {
        return -1
    }

    if nums[i] == nums[i-1] {
        return abs(leftSum - rightSum)
    } else {
        return min(abs(leftSum-rightSum), abs(leftSum-rightSum-int64(nums[i-1])*2))
    }
}

func abs(x int64) int64 {
	if x < 0 {
		return -x
	}
	return x
}