func destroyTargets(nums []int, space int) int {
    counter := make(map[int]int)
    positions := make(map[int]int)
    maxCount, minPosition := 0, math.MaxInt64

    for _, num := range nums {
        rmd := num % space
        counter[rmd]++
        if pos, exist := positions[rmd]; exist == false {
            positions[rmd] = num
        } else if num < pos {
            positions[rmd] = num
        }

        if counter[rmd] > maxCount {
            maxCount = counter[rmd]
            minPosition = positions[rmd]
        } else if counter[rmd] == maxCount && positions[rmd] < minPosition {
            minPosition = positions[rmd]
        }
    }
    return minPosition
}