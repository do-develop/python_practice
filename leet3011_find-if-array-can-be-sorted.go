func canSortArray(nums []int) bool {
    maxAttempts := len(nums) - 1
    noAttempt := 0

    for noAttempt < maxAttempts {
        for i := 0; i < len(nums) - 1; i++ {
            if nums[i] > nums[i + 1] {
                if countSetBits(nums[i]) == countSetBits(nums[i+1]) {
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    noAttempt = 0
                } else {
                    return false
                }
            } else {
                noAttempt++
            }
        }
    }
    return true
}

func countSetBits(num int) int {
    count := 0
    for num > 0 {
        count += num & 1
        num >>= 1
    }
    return count
}