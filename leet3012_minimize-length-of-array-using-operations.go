func minimumArrayLength(nums []int) int {
    mini := nums[0]
    for _, n := range nums {
        if n < mini {
            mini = n
        }
    }

    for _, n := range nums {
        if n % mini != 0 {
            return 1
        }
    }

    // If all numbers are multiples of the smallest number, 
    // then the result depends on how often the minimum appears.
    count := 0
    for _, n := range nums {
        if n == mini {
            count++
        }
    }

    return (count + 1) / 2
}