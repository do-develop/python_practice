func maxSum(nums []int) int {
    positiveSet := make(map[int]bool)
    maxNum := nums[0]
    for _, num := range nums {
        if num > 0 {
            positiveSet[num] = true
        }
        maxNum = max(maxNum, num)
    }

    if len(positiveSet) == 0 {
        return maxNum
    }
    sum := 0
    for num := range positiveSet {
        sum += num
    }
    return sum
}