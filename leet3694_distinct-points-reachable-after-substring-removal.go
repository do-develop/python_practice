func distinctPoints(s string, k int) int {
    type point struct{ x, y int }
	seen := map[point]bool{{0, 0}: true}

    x, y := 0, 0
    for i := k; i < len(s); i++ {
        switch s[i] {
		case 'U':
			y++
		case 'D':
			y--
		case 'L':
			x--
		case 'R':
			x++
		}

        switch s[i-k] {
		case 'U':
			y--
		case 'D':
			y++
		case 'L':
			x++
		case 'R':
			x--
		}

        seen[point{x, y}] = true
    }
    return len(seen)
}