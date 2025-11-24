func maximumEnergy(energy []int, k int) int {
    N := len(energy)
    ans := -1 << 31

    for i := N - k; i < N; i++ {
        total := 0
        for j := i; j >= 0; j -= k {
            total += energy[j]
            ans = max(ans, total)
        }
    }
    return ans
}