func maxFrequencyElements(nums []int) int {
    frequency := make(map[int]int)

    for _, num := range nums {
        frequency[num]++
    }

    count := 0
    maxFreq := -1

    for _, freq := range frequency {
        if freq > maxFreq {
            maxFreq = freq
        }
    }

    for _, freq := range frequency {
        if freq == maxFreq {
            count += maxFreq
        }
    }
    return count
}