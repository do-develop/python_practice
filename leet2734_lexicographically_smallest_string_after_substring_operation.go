func smallestString(s string) string {
    pos, N := 0, len(s)

    for pos < N {
        if s[pos] != 'a' {
            break
        }
        pos++
    }

    // all 'a's
    if pos == N {
        return s[:N - 1] + "z"
    }

    ans := []byte(s)
    for i := pos; i < N; i++ {
        if ans[i] == 'a' {
            break
        }
        ans[i] = ans[i] - 1
    }
    return string(ans)
}