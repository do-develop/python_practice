func minSwaps(nums []int) int {
    N := len(nums)

    order := make([]int, N)
    for i := range order {
        order[i] = i
    }
    slices.SortFunc(order, func(i, j int) int {
        si, sj := digitSum(nums[i]), digitSum(nums[j])
        if si != sj {
            return si - sj
        }
        return nums[i] - nums[j]
    })

    swaps := 0
    for cur, target := range order {
        for cur != target {
            order[cur], order[target] = order[target], order[cur]
            target = order[cur]
            swaps++
        }
    }
    return swaps
}

func digitSum(x int) int {
    total := 0
    for x > 0 {
        total += x % 10
        x /= 10
    }
    return total
}