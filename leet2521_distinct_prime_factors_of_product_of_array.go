func distinctPrimeFactors(nums []int) int {
    factors := make(map[int]int)
    for _, n := range nums {
        for i := 2; n > 1; i++ {
            for n % i == 0 {
                factors[i]++
                n = n / i
            }
        }
    }
    return len(factors)
}