func minOperations(nums []int) []int {
    res := make([]bool, 5001) // to check until the limit
    for i := 1; i <= 5000; i++ {
        str := fmt.Sprintf("%b", i)
        if checkPalindrome(str){
            res[i] = true
        } else{
            res[i] = false
        }
    }
    
    N := len(nums)
    ans := make([]int, N)
    for i := 0; i < N; i++ {
        if res[nums[i]] {
            ans[i] = 0
            continue
        }

        l, r := nums[i] - 1, nums[i] + 1
        for l >= 0 || r <= 5000 {
            if l >= 0 && res[l] {
                ans[i] = nums[i] - l
                break
            }
            if r <= 5000 && res[r] {
                ans[i] = r - nums[i]
                break
            }
            l--
            r++
        }
    }
    return ans
}

func checkPalindrome(binstr string) bool {
    for i := 0; i < len(binstr)/2; i++ {
        if binstr[i] != binstr[len(binstr)-i-1] {
            return false
        }
    }
    return true
}