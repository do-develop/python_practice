func minOperations(nums1 []int, nums2 []int) int64 {
    v := nums2[len(nums2)-1]
    ops := 0
    last := math.MaxInt64

    for i := 0; i < len(nums1); i++ {
        a, b := nums1[i], nums2[i]
        ops += abs(a - b)

        if(a <= v && v <= b) || (b <= v && v <= a) {
            last = 0
        }

        last = min(last, min(abs(v - a), abs(v - b)))
    }

    return int64(ops + last + 1)
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}