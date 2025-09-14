func minimumPushes(word string) int {
    m := make([]int, 26, 26)
    for _, c := range word {
        m [c - 97]++
    }

    sort.Slice(m, func(x, y int)bool {
        return m[x] > m[y]
    })

    ans := 0
    for i := 0; i < len(m); i++ {
        miniPush := i/8 + 1
        if m[i] > 0 {
            ans += miniPush
        }
    }
    return ans
}