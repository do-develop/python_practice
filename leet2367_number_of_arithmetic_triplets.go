func arithmeticTriplets(nums []int, diff int) int {
    triplets := 0
    i, j, k := 0, 1, 2
    N := len(nums)

    for i < N - 2 && j < N - 1 && k < N {
        if !foundPair(diff, &i, &j, &nums){
            continue
        }
        if !foundPair(diff, &j, &k, &nums){
            continue
        }
        i++
        j++
        k++
        triplets++
    }
    return triplets
}

func foundPair(diff int, l, r *int, nums *[]int) bool {
    value := (*nums)[*r] - (*nums)[*l]

    if diff > value {
        *r++
        return false
    }

    if diff < value {
        *l++
        return false
    }
    return true
}