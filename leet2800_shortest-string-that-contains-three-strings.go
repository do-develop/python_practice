func minimumString(a string, b string, c string) string {
    arr := []string{a, b, c}
    N := len(arr)
    ans := ""

    for i := 0; i < N; i++ {
        for j := 0; j < N; j++ {
            for k := 0; k < N; k++ {
                if i != j && j != k && i != k {
                    sub1 := mergeStrings(arr[i], arr[j])
                    sub2 := mergeStrings(sub1, arr[k])

                    if ans == "" || len(sub2) < len(ans) || (len(sub2) == len(ans) && strings.Compare(sub2, ans) < 0) {
                        ans = sub2
                    }
                }
                
            }
        }
    }
    return ans
}

func min(x, y int) int {
    if x < y {
        return x
    } 
    return y
} 

func mergeStrings(x, y string) string {
    if strings.Contains(x, y) {
        return x
    }

    for i := min(len(x), len(y)); i >= 0; i-- {
        if x[len(x) - i:] == y[:i] {
            return x + y[i:]
        }
    }

    return x + y
}