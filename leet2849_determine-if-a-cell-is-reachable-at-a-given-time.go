func isReachableAtTime(sx int, sy int, fx int, fy int, t int) bool {
    if sx == fx && sy == fy {
        return t == 0 || t > 1
    }

    width := abs(fx - sx)
    height := abs(fy - sy)

    return t >= int(math.Max(float64(width), float64(height)))
}

func abs(n int) int {
    if n < 0 {
        return -n
    } 
    return n
}