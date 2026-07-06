func specialTriplets(nums []int) int {
    const MOD = 1000000007
    numCount := make(map[int]int)
    numLeftCount := make(map[int]int)

    for _, v := range nums {
        numCount[v]++
    }

    ans := 0
    for _, v := range nums {
        target := v * 2
        left := numLeftCount[target]
        numLeftCount[v]++
        right := numCount[target] - numLeftCount[target]

        ans = (ans + left * right) % MOD
    }
    return ans
}