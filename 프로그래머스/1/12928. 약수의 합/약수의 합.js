function solution(n) {
    let ret = 0;
    const m = Math.ceil(n**(1/2))
    for (let i=1; i<=n; i++) {
        if (i**2 > n) break;
        if (n%i) continue;
        ret += i
        if (i**2 !== n) {
            ret += n/i
        }
    }
    return ret;
}