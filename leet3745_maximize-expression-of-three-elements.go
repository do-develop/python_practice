func maximizeExpressionOfThree(nums []int) int {
    max1, max2 := math.MinInt, math.MinInt
    min1 := nums[0]

    for _, num := range nums {
        if num > max1 {
            max2 = max1
            max1 = num
        } else if num > max2 {
            max2 = num
        }

        if num < min1 {
            min1 = num
        }
    }

    return max1 + max2 - min1
}