func maxHeightOfTriangle(red int, blue int) int {
    // simulate both case
    maxHeight := 0

    for _, colors := range[2][2]int{{red, blue}, {blue, red}} {
        a, b := colors[0], colors[1]
        level := 0
        
        for a > level {
            a -= level + 1
            level++

            if b > level {
                b -= level + 1
                level++
            } else {
                break
            }
        } 
        maxHeight = max(maxHeight, level)
    }    
    return maxHeight
}