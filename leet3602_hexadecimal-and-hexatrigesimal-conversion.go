func concatHex36(n int) string {
    n2 := n * n
    n3 := n * n * n

    hexadec := []byte("0123456789ABCDEF")
    hexatri := []byte("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    var s1 []byte
    for n2 > 0 {
        digit := n2 % 16 
        s1 = append(s1, hexadec[digit])
        n2 /= 16
    }

    var s2 []byte
    for n3 > 0 {
        digit := n3 % 36
        s2 = append(s2, hexatri[digit])
        n3 /= 36
    }

    slices.Reverse(s1)
    slices.Reverse(s2)

    return string(s1) + string(s2)
}