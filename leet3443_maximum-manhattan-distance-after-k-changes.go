func maxDistance(s string, k int) int {
    lat, lon, ans := 0, 0, 0

    for i, ch := range s {
        switch ch {
        case 'N': 
            lat++
        case 'S': 
            lat--
        case 'E':
            lon++
        case 'W':
            lon--
        }
        // capped at total steps taken so far (i + 1)
        ans = max(ans, min(abs(lat) + abs(lon) + 2*k , i + 1))
    }    
    return ans
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}