func partitionArray(nums []int, k int) bool {
    N := len(nums)

    if N % k != 0 {
        return false
    }

    freq := make(map[int]int)

    for _, x := range nums {
        freq[x]++
    }

    for _, val := range freq {
        if val * k > N {
            return false
        }
    }

    return true
}