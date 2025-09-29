func lastNonEmptyString(s string) string {
    frequency := [26]int{}
    maxFreq := 0

    for _, c := range s {
        idx := c - 'a'
        frequency[idx]++
        if frequency[idx] > maxFreq {
            maxFreq = frequency[idx]
        }
    }

    var lastStr []byte
    for i := len(s) - 1; i >=0; i-- {
        idx := s[i] - 'a'
        if frequency[idx] == maxFreq {
            //prepend to lastStr
            lastStr = append([]byte{s[i]}, lastStr...)
            frequency[idx] = 0
        }
    }
    return string(lastStr[:])
}