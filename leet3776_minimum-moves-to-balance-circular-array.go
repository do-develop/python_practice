func minMoves(balance []int) int64 {
    n := len(balance)
    pos := 0
    neg := 0
    negIndex := -1
    for i, b := range balance {
        if b > 0 {
            pos += b
        }
        if b < 0 {
            neg = b
            negIndex = i
        }
    }
    if negIndex < 0 {
        return 0
    }
    if pos < -neg {
        return -1
    }

    left := (negIndex - 1 + n) % n
    right := (negIndex + 1) % n
    leftDist, rightDist := 1, 1
    var moves int64

    for neg < 0 {
        if balance[left] > -neg {
            moves += int64(leftDist * -neg)
            return moves
        } else {
            moves += int64(leftDist * balance[left])
            neg += balance[left]
        }
        if balance[right] > -neg {
            moves += int64(rightDist * -neg)
            return moves
        } else {
            moves += int64(leftDist * balance[right])
            neg += balance[right]
        }

        left = (left - 1 + n) % n
        right = (right + 1) % n
        leftDist++
        rightDist++
    }

    return moves
}