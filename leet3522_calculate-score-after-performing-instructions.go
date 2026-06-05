func calculateScore(instructions []string, values []int) int64 {
    N := len(values)
    visited := make([]bool, N)
    var score int

    for i := 0; !visited[i]; {
        visited[i] = true
        if instructions[i] == "add" {
            score += values[i]
            i++
        } else {
            i += values[i]
        }
        if i < 0 || i >= N {
            break
        }
    }
    return int64(score)
}