func answerQueries(nums []int, queries []int) []int {
    res := make([]int, len(queries))

    // 1. sort the array
    sort.Ints(nums)
    // 2. prefix sum
    for i := 1; i < len(nums); i++ {
        nums[i] += nums[i - 1]
    }
    // 3. binary search
    for idx, query := range(queries) {
        lo, hi := 0, len(nums)

        for lo < hi {
            mid := lo + ((hi - lo) >> 1)

            if nums[mid] <= query {
                lo = mid + 1
            } else {
                hi = mid
            }
        }
        res[idx] = lo
    }

    return res
}