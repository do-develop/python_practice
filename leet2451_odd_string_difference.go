import "strconv"
import "strings"

func oddString(words []string) string {
    counter := make(map[string][]int, 2)
    for idx, word := range words {
        array := make([]string, 0, len(word) - 1)
        for i := 0; i < len(word) - 1; i++ {
            array = append(array, strconv.Itoa(int(word[i+1]) - int(word[i])))
        }
        key := strings.Join(array, ",")
        counter[key] = append(counter[key], idx)
    }
    for _, v := range counter {
        if len(v) == 1 {
            return words[v[0]]
        }
    }
    return ""
}