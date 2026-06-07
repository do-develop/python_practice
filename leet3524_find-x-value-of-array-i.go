func resultArray(nums []int, k int) []int64 {
    res := make([]int64, k)
    // counter[r] = number of subarrays ending at prev element with product%k == r
    counter := make([]int64, k)

    for _, n := range nums {
        temp := make([]int64, k)

        for rem, cnt := range counter {
            if cnt > 0 {
                newRem := (rem * n) % k
                temp[newRem] += cnt
                res[newRem] += cnt
            }
        }

        newRem := n % k
        temp[newRem]++
        res[newRem]++

        counter = temp
    }
    return res
}