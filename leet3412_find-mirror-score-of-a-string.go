func calculateScore(s string) int64 {
    var lastSeen [26][]int
    var totalScore int64

    for i := 0; i < len(s); i++ {
        ch := s[i]
        mirrorIdx := mirror(ch) - 'a'
        charIdx := ch - 'a'

        mirrorStack := lastSeen[mirrorIdx]
        hasMirrorWaiting := len(mirrorStack) > 0

        if hasMirrorWaiting {
            lastMirrorPos := mirrorStack[len(mirrorStack) - 1]
            lastSeen[mirrorIdx] = mirrorStack[:len(mirrorStack)-1] //pop
            totalScore += int64(i - lastMirrorPos)
        } else {
            lastSeen[charIdx] = append(lastSeen[charIdx], i)
        }
    }
    return totalScore
}

func mirror(c byte) byte {
    return 'z' - (c - 'a')
}