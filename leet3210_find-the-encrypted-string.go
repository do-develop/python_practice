func getEncryptedString(s string, k int) string {
    N := len(s)
    bytes := make([]byte, N)
    k = k % N

    for i := 0; i < N; i++ {
        j := (i + k) % N
        bytes[i] = s[j] 
    }
    return string(bytes)
}