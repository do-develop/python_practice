func checkStrings(s1 string, s2 string) bool {
    s1odd := make(map[byte]int, len(s1)/2)
    s1even := make(map[byte]int, len(s1)/2)
    s2odd := make(map[byte]int, len(s2)/2)
    s2even := make(map[byte]int, len(s2)/2)

    for i := range s1 {
        if i % 2 == 0 {
            s1even[s1[i]]++
            s2even[s2[i]]++
        } else {
            s1odd[s1[i]]++
            s2odd[s2[i]]++
        }
    }

    for x := byte('a'); x <= 'z'; x++ {
        if s1odd[x] != s2odd[x] || s1even[x] != s2even[x] {
            return false
        }
    }
    return true
}