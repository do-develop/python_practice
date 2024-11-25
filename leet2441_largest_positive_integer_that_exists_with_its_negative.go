func findMaxK(nums []int) int {
    seen := map[int]bool{}
    res := -1

    for _, num := range nums {
        absNum := int(math.Abs(float64(num)))

        if absNum < res {
            continue
        }

        if seen[-num] {
            res = absNum
        } else {
            seen[num] = true
        }
    }

    return res
}