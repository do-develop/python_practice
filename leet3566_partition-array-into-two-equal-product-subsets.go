func checkEqualPartitions(nums []int, target int64) bool {
    sort.Ints(nums)
    N := len(nums)

    if int64(nums[N-1]) > target {
        return false
    }

    prefix := make([]int64, N)
    prefix[0] = int64(nums[0])
    for i := 1; i < N; i++ {
        prefix[i] = prefix[i-1] * int64(nums[i])
    }

    if prefix[N-1] != target * target {
        return false
    }

    //  If the smallest ⌈n/2⌉ elements already overflow target, that smaller subset cannot exist.
    mid := (N + 1) / 2
    for _, prod := range prefix[:mid] {
        if prod > target {
            return false
        }
    }
    return true
}