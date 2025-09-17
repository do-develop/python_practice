func minimumPushes(word string) int {
    frequencies := make([]int, 26)
    for _, c := range word {
        frequencies[c - 'a']++
    }

    sort.Sort(sort.Reverse(sort.IntSlice(frequencies)))

    totalPresses := 0
    for i , freq := range frequencies {
        if freq == 0 {
            break
        }

        totalPresses += (i / 8 + 1) * freq
    }
    return totalPresses
}