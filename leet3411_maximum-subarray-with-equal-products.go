func maxLength(nums []int) int {
    n := len(nums)
	maxLen := 1

	for i := 0; i < n; i++ {
        prod := 1
        g := 0
        l := 1

        for j := i; j < n; j++ {
            prod *= nums[j]

            if j == i {
                g = nums[j]
                l = nums[j]
            } else {
                g = gcd(g, nums[j])
				l = lcm(l, nums[j])
            }

            if prod == g * l {
                length := j - i + 1
                if length > maxLen {
                    maxLen = length
                }
            }
        }
    }
    return maxLen
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func lcm(a, b int) int {
	return a / gcd(a, b) * b
}