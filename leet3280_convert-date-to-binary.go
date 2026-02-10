func convertDateToBinary(date string) string {
    parsed := strings.Split(date, "-")

    year, _ := strconv.Atoi(parsed[0])
    month, _ := strconv.Atoi(parsed[1])
    day, _ := strconv.Atoi(parsed[2])

    bYear := strconv.FormatInt(int64(year), 2)
    bMonth := strconv.FormatInt(int64(month), 2)
    bDay := strconv.FormatInt(int64(day), 2)

    return fmt.Sprintf("%s-%s-%s", bYear, bMonth, bDay)
}