func shiftingLetters(s string, shifts [][]int) string {
    var N int = len(s)
    prefix := make([]int, N + 1)
    for _, shift := range shifts {
        dir := -1
        if shift[2] == 1 { dir = 1 }
        prefix[shift[0]] += dir
        prefix[shift[1] + 1] -= dir // to stop the accumulation effect later

    }

    accumulated := 0
    shifted := make([]byte, N)
    for i := 0; i < N; i++ {
        accumulated = (accumulated + prefix[i]) % 26
        shiftedVal := (int(s[i]) - int('a') + accumulated + 26) % 26
        shifted[i] = byte(shiftedVal + int('a'))
    }

    return string(shifted)
}