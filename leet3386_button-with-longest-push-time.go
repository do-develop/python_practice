func buttonWithLongestTime(events [][]int) int {
    var idx, maxTime, lastTime int

    for _, evt := range events {
        time := evt[1] - lastTime
        if maxTime < time || (maxTime==time && idx > evt[0]) {
            maxTime = time
            idx = evt[0]
        }
        lastTime = evt[1]
    }
    return idx
}