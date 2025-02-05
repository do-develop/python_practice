func passThePillow(n int, time int) int {
    currPos := 1
    currTime := 0
    direction := 1

    for currTime < time {
        nextPos := currPos + direction
        if 0 < nextPos && nextPos <= n {
            currPos += direction
            currTime++
        } else {
            direction *= -1
        }
    }
    return currPos
}