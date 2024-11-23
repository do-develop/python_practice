func robotWithString(s string) string {
    N := len(s)
    count := make(map[rune]int)

    for i:=0; i<N; i++ {
        count[rune(s[i])]++
    }

    paper := []rune{}
    t := []rune{}

    for i:=0; i<N; i++ {
        c := rune(s[i])

        if isSmallest(c, count) {
            paper = append(paper, c)
        } else {
            t = append(t, c)
        }
        count[c]--

        for len(t) > 0 && isSmallest(t[len(t)-1], count){
            paper = append(paper, t[len(t) -1])
            t = t[:len(t) - 1]
        }
    }

    return string(paper)
}

func isSmallest(x rune, count map[rune]int) bool {
    for i := 'a'; i < x; i++ {
        if v, ok := count[i]; ok && v > 0 {
           return false 
        }
    }
    return true
}