function solution(n) {
    ret = 0;
    for (let i=2; i<=n; i+=2) {
        ret += i;
    }
    return ret;
}