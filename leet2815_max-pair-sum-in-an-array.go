func maxSum(nums []int) int {
    maxMap := make(map[int]int)
    mxSum := -1

    for _, num := range nums {
        mx := maxDigit(num)
        if val, exists := maxMap[mx]; exists {
            mxSum = maxVal(mxSum, num+val)
            if num > val {
                maxMap[mx] = num
            }
        } else {
            maxMap[mx] = num
        }
    }
    return mxSum
}


func maxVal(x, y int) int {
    if x > y {
        return x
    }
    return y
}

func maxDigit(n int) int {
    max := 0
    for n > 0 {
        rem := n % 10
        max = maxVal(max, rem)
        n /= 10
    }
    return max
}