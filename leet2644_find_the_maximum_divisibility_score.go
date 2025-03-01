func maxDivScore(nums []int, divisors []int) int {
    max, score := 0, 0

    for _, div := range divisors {
        currMax := 0
        for _, num := range nums {
            if num % div == 0 {
                currMax++
            }
        }
        if currMax == max {
            if div < score {
                score = div
            }
        } else if currMax > max {
            max = currMax
            score = div
        }
    }

    if max == 0 {
        sort.Ints(divisors)
        return divisors[0]
    }

    return score
}
