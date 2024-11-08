func mostFrequentEven(nums []int) int {
    counter := make(map[int]int)
    for _, num := range nums {
        if num % 2 == 0 {
            counter[num]++
        }
    }

    evenElement := -1
    maxFrequency := 0
    for key, val := range counter {
        if val > maxFrequency || (val == maxFrequency && key < evenElement) {
            maxFrequency = val
            evenElement = key
        }
    }
    return evenElement
}