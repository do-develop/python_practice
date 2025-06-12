func numberOfPoints(nums [][]int) int {
    // line sweep
    var marker[102] int
    for _, num := range nums {
        marker[num[0]]++
        marker[num[1] + 1]-- // the next of the end of the point (reduce it back)
    }
    res ,cars := 0, 0
    for _, cnt := range marker {
        cars += cnt
        if cars > 0 { //covered
            res++
        }
    }
    return res
}