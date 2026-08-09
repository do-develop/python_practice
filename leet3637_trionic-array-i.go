func isTrionic(nums []int) bool {
    N := len(nums)
    i := 1

    for i < N && nums[i - 1] < nums[i] {
        i++
    }

    p := i - 1
    for i < N && nums[i - 1] > nums[i] {
        i++
    }

    q := i - 1
    for i < N && nums[i - 1] < nums[i] {
        i++
    }

    flag := i - 1
    return p != 0 && p != q && flag != q && flag == N - 1 
}