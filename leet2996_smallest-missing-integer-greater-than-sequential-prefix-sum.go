func missingInteger(nums []int) int {
    sum := nums[0]

    for i := 1; i < len(nums); i++ {
        if nums[i] != nums[i - 1] + 1 {
            break
        }
        sum += nums[i]
    }

    sort.Ints(nums)
    for _, num := range nums {
        if num == sum {
            sum++
        }
    }
    return sum
}