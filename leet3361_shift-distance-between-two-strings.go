func shiftDistance(s string, t string, nextCost []int, previousCost []int) int64 {
    cost := 0

    for i := 0; i < len(s); i++ {
        if s[i] == t[i] {
            continue
        }

        curr := int(s[i] - 'a')
        target := int(t[i] - 'a')

        forward := 0
        diff := (target - curr + 26) % 26
        for j := 0; j < diff; j++ {
            forward += nextCost[(curr + j + 26) % 26]
        }

        backward := 0
        diff = (curr - target + 26) % 26
        for j := 0; j < diff; j++ {
            backward += previousCost[(curr - j + 26) % 26]
        }
        cost += min(forward, backward)
    }
    return int64(cost)
}