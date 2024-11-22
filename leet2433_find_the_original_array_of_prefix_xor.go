func findArray(pref []int) []int {
    N := len(pref)
    arr := make([]int, N)
    arr[0] = pref[0]

    for i:=1; i<N; i++ {
        arr[i] = pref[i-1] ^ pref[i]
    }
    return arr
}