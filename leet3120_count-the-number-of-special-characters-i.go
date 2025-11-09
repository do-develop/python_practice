func numberOfSpecialChars(word string) int {
    exist := make(map[rune]bool)

    for _, char := range word {
        exist[char] = true
    }

    count := 0
    for key, _ := range exist {
        if exist[key] && exist[key-32] {
            count++
        }
    }
    return count
}