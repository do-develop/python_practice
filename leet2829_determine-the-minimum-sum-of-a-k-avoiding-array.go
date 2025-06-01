func minimumSum(n int, k int) int {
    set := hashset.New() // to keep track of already added numbers

    for i := 1; set.Size() != n; i++ {
        if !set.Contains(k - i) {
            set.Add(i)
        }
    }

    var total int
    for _, v := range set.Values() {
        total += v.(int)
    }
    return total
}