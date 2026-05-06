func sumOfGoodNumbers(nums []int, k int) int {
    total := 0
    N := len(nums)

    for i, num := range nums {
        condition1 := i - k > -1 && nums[i-k] >= num
        condition2 := i + k < N && nums[i+k] >= num
        if condition1 || condition2 {
            continue
        }
        total += num
    }
    return total
}