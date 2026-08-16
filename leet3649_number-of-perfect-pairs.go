func perfectPairs(nums []int) int64 {
    n := len(nums)
    arr := make([]int, n)
    for i, x := range nums {
        if x < 0 {
            arr[i] = -x
        } else {
            arr[i] = x
        }
    }
    sort.Ints(arr)

    var cnt int64 = 0
    r := 0
    for i := 0; i < n; i++ {
        if r < i {
            r = i
        }
        for r+1 < n && arr[r+1] <= 2*arr[i] {
            r++
        }
        cnt += int64(r - i)
    }
    return cnt
}