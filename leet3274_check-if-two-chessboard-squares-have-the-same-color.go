func checkTwoChessboards(coordinate1 string, coordinate2 string) bool {
    calculated1 := (int(coordinate1[0]) - int('a') + 1 + int(coordinate1[1]) - int('0'))
    calculated2 := (int(coordinate2[0]) - int('a') + 1 + int(coordinate2[1]) - int('0'))

    return (calculated1 % 2) == (calculated2 % 2)
}