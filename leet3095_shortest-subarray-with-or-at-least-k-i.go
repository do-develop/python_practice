func minimumSubarrayLength(nums []int, k int) int {
    minLen := math.MaxInt

    for i := 0; i < len(nums); i++ {
        curr := 0

        for j := i; j < len(nums); j++ {
            curr |= nums[j]

            if (curr >= k && minLen > j - i + 1) {
                minLen = j - i + 1
            } 
        }
    }

    if minLen == math.MaxInt {
        return -1
    }
    return minLen
}