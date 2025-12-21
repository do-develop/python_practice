func numberOfAlternatingGroups(colors []int) int {
    N := len(colors)
    if N < 3 {
        return 0
    }

    ans := 0
    for i := 0; i < N - 2; i++ {
        if colors[i] == colors[i + 2] && colors[i] != colors[i + 1] {
            ans++
        }
    }

    if colors[0] == colors[N - 2] && colors[0] != colors[N - 1] {
        ans++
    }

    if colors[0] != colors[1] && colors[1] == colors[N - 1] {
        ans++
    }
    return ans
}