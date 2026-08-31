func minOperations(nums []int) int {
    // 0 if all values in the array are initially equal, and 1 otherwise, 
    // since you can apply the AND operation on the whole array in one step.
    N := len(nums)

    for i := 1; i < N; i++ {
        if nums[i] != nums[i-1] {
            return 1
        }
    }
    return 0
}