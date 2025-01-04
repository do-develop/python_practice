func captureForts(forts []int) int {
    captured := 0
    
    for curr, prev := 0, 0; curr < len(forts); curr++ {
        if forts[curr] != 0 {
            if forts[prev] == -forts[curr] {
                captured = max(captured, curr - prev - 1)  
            }
            prev = curr
        }
    }
    return captured
}
