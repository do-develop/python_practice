func absDifference(nums []int, k int) int {
    sort.Ints(nums)
    return total(nums[len(nums)-k:]) - total(nums[:k])
}

func total(nums []int) int {
    sum := 0
    for _, n := range nums {
        sum += n
    }
    return sum
}