func numOfSubsequences(s string) int64 {
    var noInsert, insertedL, insertedT, maxProduct int64
    var lCount, tCount int64

    for _, ch := range s {
        if ch == 'T'{
            tCount++
        }
    }

    for _, ch := range s {
        switch ch {
        case 'L':
            lCount++
        case 'T':
            tCount--
        case 'C':
            noInsert += lCount * tCount
            insertedL += (lCount + 1) * tCount
            insertedT += lCount * (tCount + 1)
        }
        if product := lCount * tCount; product > maxProduct {
            maxProduct = product
        }
    }

    best := insertedL
    if v := noInsert + maxProduct; v > best {
        best = v
    }
    if insertedT > best {
        best = insertedT
    }
    return best
}