function solution(n) {
    return `${'수박'.repeat(Math.trunc(n/2))}${n%2 ? '수' : ''}`
}