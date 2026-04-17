func maximumCoins(coins [][]int, k int) int64 {
    var slide func([][]int) int64
	slide = func(c [][]int) int64 {
		sort.Slice(c, func(i, j int) bool { return c[i][0] < c[j][0] })
		var res, win int64
		j := 0

		for i, cur := range c {
			rightBoundary := cur[0] + k
			for j+1 < len(c) && c[j+1][0] < rightBoundary {
				win += int64(c[j][1]-c[j][0]+1) * int64(c[j][2])
				j++
			}
			var partial int64
			if j < len(c) && c[j][0] < rightBoundary {
				partial = int64(min(rightBoundary-1, c[j][1])-c[j][0]+1) * int64(c[j][2])
			}
			if v := win + partial; v > res {
				res = v
			}
			win -= int64(c[i][1]-c[i][0]+1) * int64(c[i][2])
		}
		return res
	}

	neg := make([][]int, len(coins))
	for i, c := range coins {
		neg[i] = []int{-c[1], -c[0], c[2]}
	}
	return max(slide(coins), slide(neg))

}