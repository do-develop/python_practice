func maximizeSquareArea(m int, n int, hFences []int, vFences []int) int {
    hFences = append([]int{1}, append(hFences, m)...)
	vFences = append([]int{1}, append(vFences, n)...)
	sort.Ints(hFences)
	sort.Ints(vFences)
    diffs := make(map[int]bool)

    maxArea := int64(-1)
    for i := 0; i < len(hFences) - 1; i++ {
        for j := i + 1; j < len(hFences); j++ {
            diffs[hFences[j]-hFences[i]] = true
        }
    }

    for i := 0; i < len(vFences) - 1; i++ {
        for j := i + 1; j < len(vFences); j++ {
            vDiff := vFences[j]-vFences[i]
            if diffs[vDiff] {
                maxArea = max(maxArea, int64(vDiff * vDiff))
            }
        }
    }
    return int(maxArea % 1_000_000_007)
}

func max(x int64, y int64) int64 {
    if x > y {
        return x
    }
    return y
}