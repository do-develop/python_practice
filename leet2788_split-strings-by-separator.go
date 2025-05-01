func splitWordsBySeparator(words []string, separator byte) []string {
    var splitted [] string
    for _, word := range words {
        tokens := strings.Split(word, string(separator))
        for _, token := range tokens {
            if len(token) > 0 {
                splitted = append(splitted, token)
            }
        }
    }
    return splitted
}