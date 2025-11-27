func isArraySpecial(nums []int, queries [][]int) []bool {
	n := len(nums)

	// prefix[i] = number of violating positions in nums[0:i]
	prefix := make([]int, n)
	for i := 0; i < n-1; i++ {
		prefix[i+1] = prefix[i]
		if nums[i]%2 == nums[i+1]%2 {
			prefix[i+1]++
		}
	}

	res := make([]bool, len(queries))
	for i, q := range queries {
		l, r := q[0], q[1]

		if l < r {
			// If any violating index exists in [l, r-1], prefix will increase
			res[i] = prefix[r] == prefix[l]
		} else {
			res[i] = true
		}
	}

	return res
}
