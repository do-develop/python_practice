func countSubarrays(nums []int, k int) int64 {
    maxElement := 0

    for _, val := range(nums) {
        if maxElement < val {
            maxElement = val
        }
    }

    ans, start, count := 0, 0, 0

    for _, num := range(nums) {
        if num == maxElement {
            count++
        }
        for count == k {
            if nums[start] == maxElement {
                count--
            }
            start++
        }
        // count all the valid subarrays that end at the current number in one go
        ans += start
    }
    return int64(ans)
}