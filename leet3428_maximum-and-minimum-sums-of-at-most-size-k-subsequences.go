const MOD = 1_000_000_007

func minMaxSums(nums []int, k int) int {
    sort.Ints(nums)
    N := len(nums)

    C := make([][]int, N + 1)
    for i := range C {
        C[i] = make([]int, N + 1)
        C[i][0] = 1
        for j := 1; j <= i; j++ {
            C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD
        }
    }


    // number of ways to choose 0..k-1 items from m items
    prefixComb := func(m int) int {
        res := 0
        for j := 0; j < k && j <= m; j++ {
            res = (res + C[m][j]) %  MOD
        }
        return res
    }

    ans := 0
    for i := 0; i < N; i++ {
        right := N - 1 - i
        left := i

        // nums[i] as minimum
        asMin := prefixComb(right)
        // nums[i] as maximum
        asMax := prefixComb(left)

        contrib := (asMin + asMax) % MOD
        ans = (ans + nums[i]%MOD*contrib) % MOD
    }
    return ans
}