func categorizeBox(length int, width int, height int, mass int) string {
    isBulky := isBulkyDim(length) || isBulkyDim(width) || isBulkyDim(height) || isBulkyVolume(length, width, height)
    isHeavy := mass >= 100
    if (isBulky && isHeavy) {
        return "Both"
    } 
    if isBulky {
        return "Bulky"
    }
    if isHeavy {
        return "Heavy"
    }
    return "Neither"
}

func isBulkyDim(dim int) bool {
    return dim >= 10000
}

func isBulkyVolume(a, b, c int) bool {
    x, y, z := int64(a), int64(b), int64(c)
    const threshold int64 = 1_000_000_000

    if x * y >= threshold {
        return true
    }
    return x * y * z >= threshold
}