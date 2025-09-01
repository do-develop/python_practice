func maximumLength(s string) int {
    res := -1
    lengths := make([][]int, 26)

    for i := 0; i < 26; i++ {
        lengths[i] = make([]int, len(s) + 1)
    }

    char, curr := byte(0), 0
    for i := 0; i < len(s); i++ {
        if s[i] == char {
            curr++
            lengths[char - 'a'][curr]++
        } else {
            curr = 1
            char = s[i]
            lengths[char - 'a'][curr]++
        }
    }

    for i := 0; i < 26; i++ {
        count := 0
        for j := len(s); j > 0; j-- {
            if lengths[i][j] == 0 {
                continue
            }

            count += lengths[i][j]
            if count >= 3{
                res = max (res, j)
                break
            }
        }
    }
    return res
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}