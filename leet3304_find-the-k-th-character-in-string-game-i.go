func kthCharacter(k int) byte {
    ans := []rune{'a'}

    for len(ans) < k {
        n := len(ans)
        for i := 0; i < n; i ++ {
            next := ans[i] + 1
            if next > 'z' {
                next = 'a'
            }
            ans = append(ans, next)
        }
    }
    return byte(ans[k - 1])
}