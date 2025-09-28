func maxOperations(nums []int) int {
    N := len(nums)

    if N < 2 {
        return 0
    }

    ops := 1
    opVal := nums[0] + nums[1]

    for i := 2; i <= N - 2; i += 2 {
        if nums[i] + nums[i + 1] != opVal {
            return ops
        }
        ops++
    }

    return ops
}