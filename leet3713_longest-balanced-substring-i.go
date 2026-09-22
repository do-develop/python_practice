func longestBalanced(s string) int {
    N := len(s)
    longest := 0

    for i := 0; i < N; i++ {
        counter := make([]int, 26)

        for j := i; j < N; j++ {
            c := s[j] - 'a'
            counter[c]++
            flag := true

            for _, x := range counter {
                if x > 0 && x != counter[c] {
                    flag = false
                    break
                }
            }

            if flag && (j - i + 1) > longest {
                longest = j - i + 1
            }
        }
    }
    return longest
}