func areaOfMaxDiagonal(dimensions [][]int) int {
    // Diagonal of rectangle is sqrt(length2 + width2)
    maxDiagonal := 0
    maxArea := 0

    for _, dim := range dimensions {
        length := dim[0]
        width := dim[1]
        diagonal := length * length + width * width
        area := length * width

        if diagonal > maxDiagonal {
            maxDiagonal = diagonal
            maxArea = area
        } else if diagonal == maxDiagonal {
            if area > maxArea {
                maxArea = area
            }
        }
    }
    return maxArea
}