func numberOfChild(n int, k int) int {
    rounds := k / (n - 1)
    rem := k % (n - 1)

    if rounds % 2 == 0 {
        return rem
    } else { // ball is passed backwards
        return n - rem - 1
    }
}