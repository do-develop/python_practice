func longestEqualSubarray(nums []int, k int) int {
    count := make(map[int]int)
    maxFreq := 0
    left := 0

    for right := 0; right < len(nums); right++ {
        count[nums[right]]++
        if count[nums[right]] > maxFreq {
            maxFreq = count[nums[right]]
        }

        // if the number of elemnts to change > k
        if (right - left + 1 - maxFreq) > k {
            count[nums[left]]--
            left++
        }
    }
    return maxFreq
}