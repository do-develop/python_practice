func numberOfGoodSubarraySplits(nums []int) int {
    mod := 1000000007
    ans := 1
    count, i := 0, 0

    // Skip leading zeros, since a valid split starts from '1'
    for i < len(nums) && nums[i] == 0 {
        i++
    }
    if i >= len(nums) {
        return 0
    }

    for i < len(nums) {
        if nums[i] == 1 {
            ans = (ans * (count + 1)) % mod
            count = 0
        } else {
            count++
        }
        i++
    }
    return ans
}