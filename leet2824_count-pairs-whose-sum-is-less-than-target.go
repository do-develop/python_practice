func countPairs(nums []int, target int) int {
    sort.Slice(nums, func(i, j int) bool {
        return nums[i] < nums[j]
    })

    l, r := 0, len(nums) - 1
    count := 0

    for l < len(nums) {
        if nums[l] + nums[r] < target {
            count += (r - l)
            l++
        } else {
            r--
        }

        if l == r {
            break
        }
    }
    return count
}