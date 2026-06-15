func maxFreqSum(s string) int {
    freq := make(map[byte]int)
	for i := 0; i < len(s); i++ {
		freq[s[i]]++
	}

    vowel, consonant := 0, 0

    for ch := 'a'; ch <= 'z'; ch++ {
        count := freq[(byte(ch))]
        if isVowel(byte(ch)) {
            vowel = max(vowel, count)
        } else {
            consonant = max(consonant, count)
        }
    }
    return vowel + consonant
}

func isVowel(c byte) bool {
	return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
}