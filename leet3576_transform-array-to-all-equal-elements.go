func canMakeEqual(nums []int, k int) bool {
    check := func(target int) bool {
        ops := 0
        arr := make([]int, len(nums))
        copy(arr, nums)

        for i := 0; i < len(arr) - 1; i++ {
            if arr[i] != target {
                arr[i] *= -1
                arr[i+1] *= -1
                ops++
            }
        }

        return arr[len(arr)-1] == target && ops <= k
    }
     
    return check(1) || check(-1)
}