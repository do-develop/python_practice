func maxPointsInsideSquare(points [][]int, s string) int {
    minis := make(map[rune]int)
    secondMini := math.MaxInt32
    count := 0

    for i := 0; i < len(points); i++ {
        radius := int(math.Max(math.Abs(float64(points[i][0])), math.Abs(float64(points[i][1]))))
        char := rune(s[i])

        if _, exists := minis[char]; !exists {
            minis[char] = radius
        } else if radius < minis[char] {
            if minis[char] < secondMini {
                secondMini = minis[char]
            }
            minis[char] = radius
        } else if radius < secondMini {
            secondMini = radius
        }
    }

    for _, miniRadius := range minis {
        if miniRadius < secondMini {
            count++
        }
    }
    return count
}