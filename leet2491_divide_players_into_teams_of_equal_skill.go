func dividePlayers(skill []int) int64 {
    sort.Ints(skill)

    var result int64
    sum := skill[0] + skill[len(skill) - 1]

    for i, j := 0, len(skill)-1; i < j; i, j = i + 1, j - 1 {
        if (skill[i] + skill[j]) != sum { return -1 }
        result += int64(skill[i] * skill[j])
    }
    return result
}