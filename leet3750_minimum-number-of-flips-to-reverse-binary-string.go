func minimumFlips(n int) int {
    s := []byte(fmt.Sprintf("%b", n))

    var flips int
    l, r := 0, len(s) - 1

    for l < r {
        if s[l] != s[r] {
            s[l], s[r] = s[r], s[l]
            flips += 2
        }

        l++
        r--
    }
    return flips
}