func largestInteger(nums []int, k int) int {
    largest := -1

    freq := [51]int{}
    for i, n := range nums {
        freq[n] += min(i+1, len(nums)-i, k)
        largest = max(largest, n)
    } 

    if k == len(nums) {
		return largest
	}

    for i := 50 ; i >=0 ; i-- {
        if freq[i] == 1 {
            return i
        }
    }
    return -1
}