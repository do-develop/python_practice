func sumDigitDifferences(nums []int) int64 {
    var digits int = len(strconv.Itoa(nums[0]))
    var counter = make([][10]int, digits)
    for _, num := range nums {
        for i := 0; num > 0; num /= 10 {
            counter[i][num % 10]++
            i++
        }
    }

    N := len(nums)
    total := 0

    for i := 0; i < digits; i++ {
        for _, cnt := range counter[i] {
            total += ((N - cnt) * cnt)
        }
    }

    return int64(total / 2)
}