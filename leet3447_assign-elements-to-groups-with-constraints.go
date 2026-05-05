import "math"

func assignElements(groups []int, elements []int) []int {
    m := make(map[int]int)
    for i, e := range elements {
        if _, exists := m[e]; !exists {
            m[e] = i
        }
    }

    assigned := make([]int, len(groups))
    for i, g := range groups {
        assigned[i] = check(g, m)
    }
    return assigned
}

func check(n int, m map[int]int) int {
    best := math.MaxInt32

    // only need to loop i up to sqrt(n)
    // because divisors come in PAIRS: (i, n/i)
    for i := 1; i*i <= n; i++ {
        if n%i == 0 {
            if idx, ok := m[i]; ok {
                if idx < best {
                    best = idx
                }
            }

            // n/i is the PAIRED divisor
            other := n / i
            if other != i {
                if idx, ok := m[other]; ok {
                    if idx < best {
                        best = idx
                    }
                }
            }
        }
    }

    if best == math.MaxInt32 {
        return -1
    }
    return best
}