func stableMountains(height []int, threshold int) []int {
    mountains := []int{}

    for i := 1; i < len(height); i++ {
        if height[i - 1] > threshold {
            mountains = append(mountains, i)
        }
    }
    return mountains
}