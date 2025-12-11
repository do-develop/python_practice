func valueAfterKSeconds(n int, k int) int {
    mod := 1000_000_007
    values := make([]int, n)

    for i := range values {
        values[i] = 1
    }

    for itr := 0; itr < k; itr++ {
        for idx := 1; idx < n; idx++ {
            values[idx] = (values[idx] + values[idx - 1]) % mod
        }
    }

    return values[n - 1]
}