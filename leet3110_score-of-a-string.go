func scoreOfString(s string) int {
    score := 0

    for i, char := range s {
        if i != 0 {
            score += abs(int(s[i - 1]) - int(char))
        }
    }
    return score
}

func abs(x int) int{
    if x < 0 {
        return -x
    }
    return x
}