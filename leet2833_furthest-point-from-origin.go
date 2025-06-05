func furthestDistanceFromOrigin(moves string) int {
    var left, right, direction int

    for _, move := range moves {
        if move == 'L' {
            left++
        } else if move == 'R' {
            right++
        } else {
            direction++
        }
    }
    return direction + (max(left, right) - min(left, right))
}