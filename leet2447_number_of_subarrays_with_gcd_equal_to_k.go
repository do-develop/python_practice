func subarrayGCD(nums []int, k int) int {
    N := len(nums)
    result := 0
    for idx := range nums {
        currGCD := 0
        for jdx := idx; jdx < N; jdx++ {
            currGCD = gcd(currGCD, nums[jdx])
            if currGCD == k {
                result++
            } // No need to have else condition as currGCD will only get smaller
        }
    }
    return result
}

func gcd(a, b int) int {
    if a == 0 {
        return b
    }
    return gcd(b % a, a)
}
