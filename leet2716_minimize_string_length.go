func minimizedStringLength(s string) int {
    freq := [26]int{}

    for _,c := range s {
        freq[c - 'a']++
    }

    count := 0 
    for _, f := range freq {
        if f > 0 {
            count++
        }
    }
    return count
}