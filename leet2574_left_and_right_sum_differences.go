func leftRightDifference(nums []int) []int {
    rightSum := 0
    for _, num := range nums {
        rightSum += num
    }

    leftSum := 0
    for i, num := range nums {
        nums[i] = Abs(rightSum - leftSum - num, leftSum)
        leftSum += num
    }
    return nums
}

func Abs(a, b int) int {
    if a > b {
        return a - b
    }
    return b - a
}