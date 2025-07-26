func findKOr(nums []int, k int) int {
    maxNum := 0
    for _, n := range nums {
        if n > maxNum {
            maxNum = n
        }
    }

    res := 0
    // iterate through each bit position
    for i := 1; i <= maxNum; i = i << 1 {
        count := 0

        for _, num := range nums {
            if num & i != 0 { // check if the bit i is set in num
                count++
            }
        }

        if count >= k {
            res |= i   // OR it into the result
        }
    }
    return res
}