func countBeautifulPairs(nums []int) int {
    count := 0

    for i := 0; i < len(nums); i++ {
        first := nums[i]
        for first > 9 {
            first /= 10
        }

        for  j := i + 1; j < len(nums); j++ {
            last := nums[j]
            for last > 9 {
                last %= 10
            }
            if calculateGCD(first, last) == 1 {
                count++
            }
        }       
    }
    return count
}

func calculateGCD(x, y int) int {
    for y != 0 {
        x, y = y, x % y
    }
    return x
}