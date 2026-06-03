func findClosest(x int, y int, z int) int {
    distance1 := int(math.Abs(float64(x - z)))
    distance2 := int(math.Abs(float64(y - z)))

    if distance1 < distance2 {
        return 1
    } else if distance1 > distance2 {
        return 2
    } else {
        return 0
    }
}