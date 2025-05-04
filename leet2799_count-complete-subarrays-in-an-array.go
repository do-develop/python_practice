func countCompleteSubarrays(nums []int) int {
    // sliding window approach
    count, left := 0, 0
    freq, uniq := make(map[int]int), make(map[int]struct{})

    for _, n := range nums {
        uniq[n] = struct{}{}
    }
    k := len(uniq)

    for right, n := range nums {
        freq[n]++
        for k == len(freq) {
            freq[nums[left]]--
            if freq[nums[left]] == 0 {
                delete(freq, nums[left])
            }
            count += len(nums) - right
            left++
        }
    }
    return count
}