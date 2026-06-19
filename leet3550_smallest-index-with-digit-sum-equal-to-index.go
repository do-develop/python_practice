func smallestIndex(nums []int) int {
    for i, n := range nums {
        if i == digitSum(n) {
            return i
        }
    }
    return -1
}

func digitSum(x int) int {
    sum := 0
    for x > 0 {
        sum += x % 10
        x /= 10
    }
    return sum
}