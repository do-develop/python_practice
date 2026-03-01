func minBitwiseArray(nums []int) []int {
    for i, n := range nums {
        res := -1
        curr := 1
        for (n & curr) != 0 {
            res = n - curr // change the bit into 0
            curr <<= 1
        }
        nums[i] = res
    }
    return nums
}