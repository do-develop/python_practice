func minSizeSubarray(nums []int, target int) int {
    N := len(nums)
    var sum int
    for _, num := range nums {
        sum += num
    }    

    repeats := target / sum
    target = target % sum

    if target == 0 {
        return N * repeats
    }

    res := math.MaxInt32
    var left, subSum int

    for right := 0; right < 2 * N; right++ {
        subSum += nums[right % N]
        for left < right && subSum > target {
            subSum -= nums[left % N]
            left++
        }
        if subSum == target {
            res = min(res, right - left + 1)
        }
    }
    
    if res == math.MaxInt32 {
        return -1
    }
    return repeats * N + res
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}