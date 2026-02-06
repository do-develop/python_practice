func generateKey(num1 int, num2 int, num3 int) int {
    x, ans := 1, 0
    for num1 > 0 && num2 > 0 && num3 > 0 {
        ans += x * slices.Min([]int{num1 % 10, num2 %10, num3 % 10})
        num1 /= 10
        num2 /= 10
        num3 /= 10
        x *= 10
    }
    return ans
}