func numberOfSubsequences(nums []int) int64 {
    N := len(nums)
    cnt := make(map[float64]int64)
    var res int64

    // r is the index of the third element in (p, q, r, s)
    for r := 4; r < N-2; r++ {
        q := r - 2 // sweep trick
        // As r moves right by 1, q moves right by 1 too, 
        // then only need to add one new p to the map (the new q-1)

        for p := 0; p < q - 1; p++ {
            cnt[float64(nums[p])/float64(nums[q])]++
        }

        for s := r + 2; s < N; s++ {
            res += cnt[float64(nums[s])/float64(nums[r])]
        }
    }
    return res
}