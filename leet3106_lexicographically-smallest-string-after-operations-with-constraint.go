func getSmallestString(s string, k int) string {
    result := make([]byte, len(s))

    for i := 0; i < len(s); i++ {
        ch := s[i]

        distToA := int(ch - 'a')
        distToZ := int('z' - ch + 1)
        minDist := distToA
        if distToZ < distToA {
            minDist = distToZ
        }

        if k >= minDist {
            result[i] = 'a'
            k -= minDist
        } else {
            // Move backward by k steps
            result[i] = byte(int(ch) - k)
            k = 0
        }
    }
    return string(result)
}
