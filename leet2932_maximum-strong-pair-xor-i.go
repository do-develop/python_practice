func maximumStrongPairXor(nums []int) int {
    result := 0

    for i := range nums {
        for j := i; j < len(nums); j++ {
            if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]) {
                result = max(result, nums[i] ^ nums[j])
            }
        }
    }
    return result
}

func abs(num int) int {
    if num < 0 {
        return -num
    }
    return num
}