func getSubarrayBeauty(nums []int, k int, x int) []int {
    // sliding window approach
    freq := make([]int, 51)
    ans  := []int{}
    left := 0

    for right := 0; right < len(nums); right++ {
        if nums[right] < 0 {
            freq[abs(nums[right])]++
        }

        if right - left + 1 >= k {
            cnt := 0

            for n := 50; n >= 0; n-- {
                cnt += freq[n]
                if cnt >= x {
                    ans = append(ans, -n)
                    break
                }
            }

            if cnt < x {
                ans = append(ans, 0)
            }
            if nums[left] < 0 {
                freq[abs(nums[left])]--
            }
            left++
        }
    }    
    return ans
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}
