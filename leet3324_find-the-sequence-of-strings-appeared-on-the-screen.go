func stringSequence(target string) []string {
    seq := []string{}
    
    for x := range target {
        for y := byte('a'); y <= target[x]; y++ {
            seq = append(seq, target[:x]+string(y))
        }
    }
    return seq
}