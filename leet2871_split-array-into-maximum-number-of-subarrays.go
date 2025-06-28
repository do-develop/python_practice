func minOperations(nums []int) int {
    freqMap := make(map[int]int)

    for _, val := range nums {
        freqMap[val]++
    }

    operations := 0

    for _, freq := range freqMap {
        if freq == 1 {
            return -1
        }
        operations += int(math.Ceil(float64(freq) / 3.0))
    }
    return operations
}