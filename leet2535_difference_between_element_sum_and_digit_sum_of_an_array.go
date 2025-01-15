func differenceOfSum(nums []int) int {
    elemSum, digitSum := 0, 0

        for _, num := range nums {
            elemSum += num

            for num != 0 {
                digit := num % 10
                num /= 10
                digitSum += digit
            }
        }

        return elemSum - digitSum
}