func sumIndicesWithKSetBits(nums []int, k int) int {
    var total int

    for i, v := range nums {
        if binSum(i) == k {
            total += v
        }
    }
    return total
}

func binSum(num int) int {
    var total int

    for num > 0 {
        if num % 2 == 1 {
            total++
        }
        num /= 2
    }

    return total
}