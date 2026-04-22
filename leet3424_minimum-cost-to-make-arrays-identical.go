func minCost(arr []int, brr []int, k int64) int64 {
    N := len(arr)

    var costNoSort int64
    for i := 0; i < N; i++ {
        costNoSort += int64(math.Abs(float64(arr[i] - brr[i])))
    }

    // Cost with rearranging
    arrSorted := make([]int, N)
    brrSorted := make([]int, N)
    copy(arrSorted, arr)
    copy(brrSorted, brr)
    sort.Ints(arrSorted)
    sort.Ints(brrSorted)

    // sort  is one atomic action as it can be placed in any permutation
    var costWithSort int64 = k 
    for i := 0; i < N; i++ {
        costWithSort += int64(math.Abs(float64(arrSorted[i] - brrSorted[i])))
    }

    if costNoSort < costWithSort {
        return costNoSort
    }
    return costWithSort
}