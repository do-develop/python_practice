func maxPalindromesAfterOperations(words []string) int {
    lengths := make([]int, len(words))
    counter := make(map[rune]int)

    for i, word := range words {
        lengths[i] = len(word)
        for _, c := range word {
            counter[c - 'a']++
        }
    }

    palindromes, pairCount := 0, 0
    for _, cnt := range counter {
        pairCount += cnt/2
    }
    // words are processed from shortest to longest
    sort.Ints(lengths)

    for _, length := range lengths {
        if length == 1 {
            palindromes++
        } else {
            // the number of pairs needed
            pair := length/2 
            if pairCount >= pair {
                pairCount -= pair
                palindromes++
            }
        }
    }
    return palindromes
}