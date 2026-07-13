func maxArea(coords [][]int) int64 {
    solve := func(pts [][2]int) int {
		groups := make(map[int][]int)
		xmin, xmax := pts[0][0], pts[0][0]
		for _, p := range pts {
			x, y := p[0], p[1]
			groups[x] = append(groups[x], y)
			if x < xmin {
				xmin = x
			}
			if x > xmax {
				xmax = x
			}
		}

		best := -1
		for x, ys := range groups {
			ymin, ymax := ys[0], ys[0]
			for _, y := range ys {
				if y < ymin {
					ymin = y
				}
				if y > ymax {
					ymax = y
				}
			}
			d := xmax - x
			if x-xmin > d {
				d = x - xmin
			}
			area := d * (ymax - ymin)
			if area > best {
				best = area
			}
		}
		return best
	}

	// original (x, y) pairs
	pts1 := make([][2]int, len(coords))
	// swapped (y, x) pairs
	pts2 := make([][2]int, len(coords))
	for i, c := range coords {
		pts1[i] = [2]int{c[0], c[1]}
		pts2[i] = [2]int{c[1], c[0]}
	}

	ans := solve(pts1)
	if ans2 := solve(pts2); ans2 > ans {
		ans = ans2
	}
	if ans <= 0 {
		return -1
	}
	return int64(ans)
}