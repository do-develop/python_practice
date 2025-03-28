func semiOrderedPermutation(nums []int) int {
    var x, y int
    N := len(nums)
    for idx, num := range nums {
        if num == 1 {
            x = idx
        } else if num == N {
            y = idx
        }
    }

    if x < y {
        return x + (N - y - 1)
    }
    return x + (N - y - 1) - 1
}