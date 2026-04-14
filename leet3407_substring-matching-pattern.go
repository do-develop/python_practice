func hasMatch(s string, p string) bool {
    idx := strings.Index(p, "*")
    prefix, suffix := p[:idx], p[idx+1:]

    start := strings.Index(s, prefix)
    if start == -1 {
        return false
    }

    remaining := s[start + len(prefix):]
    return strings.Contains(remaining, suffix)
}