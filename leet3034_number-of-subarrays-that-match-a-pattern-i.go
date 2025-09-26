func countMatchingSubarrays(nums []int, pattern []int) int {
    patternLen := len(pattern)
    matchCount := 0

    for i := 0; i < len(nums) - patternLen; i++ {
        var isValid bool
        for k := 0; k < patternLen; k++ {
            curr := nums[i + k]
            next := nums[i + k + 1]

            switch pattern[k] {
                case 1:
                    isValid = next > curr
                case 0:
                    isValid = next == curr
                case -1:
                    isValid = next < curr
            }
            if !isValid {
                break
            }
        }
        if isValid {
            matchCount++
        }
    }
    return matchCount
}