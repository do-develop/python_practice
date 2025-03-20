func makeSmallestPalindrome(s string) string {
    palindrome := []byte(s)

    for i, j := 0, len(palindrome) - 1; i < j; i, j = i + 1, j - 1 {
        if palindrome[i] < palindrome[j] {
            palindrome[j] = palindrome[i]
        } else {
            palindrome[i] = palindrome[j]
        }
    }

    return string(palindrome)
}