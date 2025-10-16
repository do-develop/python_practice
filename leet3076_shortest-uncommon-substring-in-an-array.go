func shortestSubstrings(arr []string) []string {
    N := len(arr)
    shortsub := make([]string, N)

    for i := 0; i < N; i++ {
        for j := 1; j <= len(arr[i]); j++ {
            for start := 0; start + j <= len(arr[i]); start++ {
                sub := arr[i][start:start + j]
                flag := false

                for k := 0; k < N; k++ {
                    if i == k {
                        continue
                    }

                    if strings.Contains(arr[k], sub) {
                        flag = true
                        break
                    }
                }

                if !flag && (shortsub[i] == "" || shortsub[i] > sub) {
                    shortsub[i] = sub
                }
            }

            if shortsub[i] != "" {
                break
            }
        }
    }
    return shortsub
}