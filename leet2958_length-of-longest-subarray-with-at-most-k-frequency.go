func maxSubarrayLength(nums []int, k int) int {
    ans, end, start := 1, 0, 0
    N := len(nums)
    counter := make(map[int]int)

    for end < N {
        counter[nums[end]]++

        for counter[nums[end]] > k {
            counter[nums[start]]--
            start++
        }
        
        if end - start + 1 > ans {
            ans = end - start + 1
        }

        end++
    }
    return ans
}