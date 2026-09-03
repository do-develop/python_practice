func smallestAbsent(nums []int) int {
    total := 0

    for _, n := range nums {
        total += n
    }

    ans := (total / len(nums)) + 1
    for slices.Contains(nums, ans) || ans < 1 {
        ans++
    }
    return ans
}