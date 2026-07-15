func checkPrimeFrequency(nums []int) bool {
    freq := [101]int{}
    for _, n := range nums {
        freq[n]++
    }
    
    for _, val := range freq {
        if isPrimeNum(val) {
            return true
        }
    }
    return false
}

func isPrimeNum(x int) bool {
	if x < 2 {
		return false
	}
	for i := 2; i*i <= x; i++ {
		if x%i == 0 {
			return false
		}
	}
	return true
}