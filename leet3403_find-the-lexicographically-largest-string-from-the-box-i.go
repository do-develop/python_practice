func answerString(word string, numFriends int) string {
    if numFriends == 1 {
        return word
    }

    N := len(word)
    largest := ""
    for i := 0; i < N; i++ {
        largest = max(largest, word[i:min(i + N - numFriends + 1, N)])
    }
    return largest
}