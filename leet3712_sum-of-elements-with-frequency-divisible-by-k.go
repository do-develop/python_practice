func sumDivisibleByK(nums []int, k int) int {
    frequencies := [101]int{}
    for _, n := range nums {
        frequencies[n]++
    }

    sum := 0
    for num, freq := range frequencies {
        if freq % k == 0 {
            sum += num * freq
        }
    }

    return sum
}