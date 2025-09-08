func findMaximumNumber(k int64, x int) int64 {
    left, right := int64(1), int64(1e15)

    for left < right {
        mid := left + (right - left)/2
        cost := int64(0)

        for bit := int64(x); bit < 60; bit += int64(x) {
            cost += countOnesUpTo(mid, bit)
        }

        if cost > k {
            right = mid
        } else {
            left = mid + 1
        }
    }
    return left - 1
}

func countOnesUpTo(num int64, bitIndex int64) int64 {
    num++

    patternLen := int64(1) << bitIndex
    fullPatterns := num / patternLen

    result := fullPatterns * (patternLen / 2)
    remainder := num % patternLen

    if remainder > patternLen/2 {
        result += remainder - patternLen/2
    }

    return result
}