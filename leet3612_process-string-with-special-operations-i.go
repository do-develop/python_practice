func processStr(s string) string {
    var res [] rune

    for _, ch := range s {
        switch ch {
            case '*':
                if len(res) > 0 {
                    res = res[:len(res)-1]
                }
            case '#':
                temp := make([]rune, len(res))
                copy(temp, res)
                res = append(res, temp...)
            case '%':
                for i, j := 0, len(res)-1; i < j; i, j = i + 1, j - 1 {
                    res[i], res[j] = res[j], res[i]
                }
            default:
                res = append(res, ch)
        }
    }
    return string(res)
}