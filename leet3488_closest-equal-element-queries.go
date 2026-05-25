func solveQueries(nums []int, queries []int) []int {
    N := len(nums)
    left := make([]int, N)
    right := make([]int, N)
    pos := make(map[int]int)

    for i := -N; i < N; i++ {
        if i >= 0 {
            left[i] = pos[nums[i]]
        }
        pos[nums[(i+N)%N]] = i
    }

    pos = make(map[int]int)
    for i := 2*N - 1; i >= 0; i-- {
        if i < N {
            right[i] = pos[nums[i]]
        }
        pos[nums[i%N]] = i
    }

    for i := 0; i < len(queries); i++ {
        x := queries[i]
        // appears only once?
        if x - left[x] == N {
            queries[i] = -1
        } else {
            queries[i] = min(x-left[x], right[x]-x)
        }
    }
    return queries
}