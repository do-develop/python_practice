func minimumOperations(nums []int) int {
    a, b, c := 0, 0, 0
    
    for _, x := range nums {
        if x != 1 {
            a += 1
        }
        if x != 2 {
            b = min(a, b + 1)
        } else {
            b = min(a, b)
        }
        if x != 3 {
            c = min(b, c + 1)
        } else {
            c = min(b, c)
        }
    }
    return c
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}