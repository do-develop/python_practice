func minimumDeletions(word string, k int) int {
    count := make(map[rune]int)
    for _, c := range word {
        count[c]++
    }

    res := len(word)
    for _, x := range count {
        deleted := 0
        for _, y := range count {
            if x > y {
                deleted += y
            } else if y > x + k {
                deleted += y - (x + k)
            }
        }
        if deleted < res {
            res = deleted
        }
    }
    return res
}