func finalPositionOfSnake(n int, commands []string) int {
    cell := 0

    for _, cmd := range commands {
        switch cmd {
            case "UP":
                cell -= n
            case "RIGHT":
                cell += 1
            case "DOWN":
                cell += n
            case "LEFT":
                cell -= 1
            
        }
    }
    return cell
}