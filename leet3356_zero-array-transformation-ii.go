func minZeroArray(nums []int, queries [][]int) int {
    N := len(nums)
    sum, k := 0, 0 

    diffArr := make([]int, N + 1)
    for idx := 0; idx < N; idx++ {
        // sum + diffArr[idx] means actual decrement
        for sum + diffArr[idx] < nums[idx] {
            k++
            if k > len(queries) {
				return -1
			}
			// Get the current query
			left := queries[k-1][0]
			right := queries[k-1][1]
			val := queries[k-1][2]

            // skip queries that don't affect current idx
            if right >= idx {
                if left > idx {
                    diffArr[left] += val
                } else {
                    diffArr[idx] += val
                }

                if right + 1 < N {
                    diffArr[right + 1] -= val
                }
            }
        }
        sum += diffArr[idx]
    }
    return k
}