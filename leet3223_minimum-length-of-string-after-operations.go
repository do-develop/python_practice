func minimumLength(s string) int {
    frequencies := make([]int, 26)
    length := 0

    for _, char := range s {
        frequencies[char - 'a']++
    }

    for _, freq := range frequencies {
        if freq == 0 {
            continue
        }
        if freq % 2 == 0 {
            length += 2
        } else {
            length += 1
        }
    }

    return length
}