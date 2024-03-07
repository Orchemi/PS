function solution(s) {
    return s.split(' ')
        .map((word) => Array
             .from(word)
             .map((c, i) => i%2 ? c.toLowerCase() : c.toUpperCase())
             .join(''))
        .join(' ')
}