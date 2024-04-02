function solution(a, b) {
    const sumFromZero = (n) => n > 0 ? (n*(n+1))/2 : -(n*(n-1))/2;
    
    let s = a, l = b;
    if (s > l) {
        let tmp = s;
        s = l;
        l = tmp;
    }
    
    const ss = sumFromZero(s);
    const sl = sumFromZero(l);
    console.log(ss, sl);
    
    if (s >= 0) return sl - ss + s;
    return l > 0 ? ss + sl : ss - sl + l;
}