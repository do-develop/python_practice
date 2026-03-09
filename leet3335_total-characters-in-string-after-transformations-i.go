const mod = 1000_000_007

func lengthAfterTransformations(s string, t int) int {
    freq := make([]int, 26)
    for _, ch := range s {
        freq[ch - 'a']++
    }    

    for round := 0; round < t; round++ {
        nxt := make([]int, 26)
        nxt[0] = freq[25]
        nxt[1] = (freq[25] + freq[0]) % mod
        for i := 2; i < 26; i++ {
            nxt[i] = freq[i - 1]
        }
        freq = nxt
    }
    
    length := 0
    for i := 0; i < 26; i++ {
        length = (length + freq[i]) % mod
    }
    return length
}