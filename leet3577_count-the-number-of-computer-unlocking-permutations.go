func countPermutations(complexity []int) int {
    N := len(complexity)

    for i := 1; i < N; i++ {
        if complexity[i] <= complexity[0] {
            return 0
        }
    }

    ans := 1
    mod := 1000_000_007
    //  the answer is (n−1)!
    for i := 2; i < N; i++ {
        ans = ans * i % mod
    }
    return ans
}