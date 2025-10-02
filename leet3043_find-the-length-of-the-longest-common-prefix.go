func longestCommonPrefix(arr1 []int, arr2 []int) int {
    prefix := make(map[int]bool)

    for _, val := range arr1 {
        for val != 0 {
            prefix[val] = true
            val = val / 10
        }
    }

    longest := 0
    for _, val := range arr2 {
        for val != 0 {
            if _, ok := prefix[val]; ok {
                N := lenOfInt(val)
                if N > longest {
                    longest = N
                }
            }
            val = val / 10
        }
    }
    return longest
}

func lenOfInt(v int) int {
    length := 0

    for v != 0 {
        length++ 
        v = v / 10
    }
    return length
}