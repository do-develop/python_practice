func findIndices(nums []int, indexDifference int, valueDifference int) []int {
    minIdx, maxIdx := 0, 0

    for i := indexDifference; i < len(nums); i++ {
        curr := i - indexDifference
        if nums[curr] < nums[minIdx] {
            minIdx = curr
        }
        if nums[curr] > nums[maxIdx] {
            maxIdx = curr
        }

        if nums[i] - nums[minIdx] >= valueDifference {
            return []int{i, minIdx}
        }
        if nums[maxIdx] - nums[i] >= valueDifference {
            return []int{i, maxIdx}
        }
    }

    return []int{-1,-1}
}