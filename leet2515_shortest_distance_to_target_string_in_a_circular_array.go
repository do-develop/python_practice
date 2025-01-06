func closetTarget(words []string, target string, startIndex int) int {
    if words[startIndex] == target {
        return 0
    }

    wordsCount := len(words)
    left := startIndex - 1
    right := startIndex + 1
    distance := 1

    for {
        if left < 0 {
            left = wordsCount - 1
        }
        if right > wordsCount - 1 {
            right = 0
        }

        if words[left] == target || words[right] == target {
            return distance
        }

        if left == right {
            return - 1
        }

        left--
        right++
        distance++
    }
}