function solution(n) {
    let s = 1, m = 1, cnt = 2;
    const M = 1234567;
    while (cnt < n) {
        let tmp = m;
        m = (s+m) % M;
        s = tmp;
        cnt++;
    }
    return m;
}