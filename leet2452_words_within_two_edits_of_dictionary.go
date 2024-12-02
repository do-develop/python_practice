func twoEditWords(queries []string, dictionary []string) []string {
    hasTwoEdits := func(query string) bool {
        for _, word := range dictionary {
            idx, count := 0, 0
            for idx < len(word) {
                if word[idx] != query[idx] { count += 1 }
                if count > 2 { break }
                idx += 1
            }
            if count <= 2 {
                return true
            }
        }
        return false
    }

    res := []string{}

    for _, q := range queries {
        if hasTwoEdits(q) {
            res = append(res, q)
        }
    }
    return res
}