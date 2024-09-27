func maximumSum(nums []int) int {
    // Group the array elements by the sum of their digits, 
    // and find the largest two elements of each group 
    store := make(map[int][]int)
    result := -1

    for _, n := range nums {
        digitSum := calculateDigitSum(n)

        values, exist := store[digitSum]
        if !exist {
            store[digitSum] = []int{n}
        } else {
            values = append(values, n)
            sort.Sort(sort.Reverse(sort.IntSlice(values)))

            if len(values) > 2 {
                values = values[:2] // keep only the two largest 
            }
            store[digitSum] = values

            if len(values) > 1 {
                result = max(result, values[0] + values[1])
            }
        }
        
    }
    return result
}

func calculateDigitSum(n int) int {
    sum := 0
    for n != 0 {
        sum += n % 10
        n /= 10
    }
    return sum
}

func max(a, b int) int {
    if a > b{
        return a
    } 
    return b
}
