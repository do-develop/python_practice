func beautifulSubstrings(s string, k int) int {
    // prefix sum array
    vowels, consonants := make([]int, len(s)), make([]int, len(s))
    vCount, cCount := 0, 0

    for i, c := range s {
        switch c {
            case 'a', 'e', 'i', 'o', 'u':
                vCount++
            default:
                cCount++ 
        }
        vowels[i] = vCount
        consonants[i] = cCount
    }

    beautiful := 0
    for i := 0; i < len(s); i++ {
        for j := i; j < len(s); j++ {
            currV, currC := vowels[j], consonants[j]
            if i > 0 {
                currV -= vowels[i - 1]
                currC -= consonants[i - 1]
            }

            if currV != currC {
                continue
            }

            if (currV * currC) % k != 0 {
                continue
            }
            beautiful++
        }
    }
    return beautiful
}