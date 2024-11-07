func checkDistances(s string, distance []int) bool {
    alphabetDist := make([]int, 26, 26)
    for i:=0; i < len(s); i++ {
        letter := int(s[i] - 'a')
        if alphabetDist[letter] == 0 {
            alphabetDist[letter] = i + 1
            continue
        }
        alphabetDist[letter] = i - alphabetDist[letter]
        if alphabetDist[letter] != distance[letter] {
            return false
        }
    }
    return true
}