func findNonMinOrMax(nums []int) int {
    if len(nums) < 3 {
        return -1
    }

    part := nums[:3] // doesn't need all
    sort.Ints(part)
    return part[1]
}