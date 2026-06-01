func minimumPairRemoval(nums []int) int {
    N := len(nums)
    arr := make([]int, N)
    copy(arr, nums)
    ops := 0

    for {
        isAscending := true
        minSum := math.MaxInt
        idx := -1 

        for i := 0; i < len(arr) - 1; i++ {
            if arr[i] > arr[i + 1] {
                isAscending = false
            }
            s := arr[i] + arr[i+1]
            if s < minSum {
                minSum = s
                idx = i
            }
        }

        if isAscending {
            break
        }

        arr[idx] = minSum
        arr = append(arr[:idx+1], arr[idx+2:]...)
        ops++
    }
    return ops
}