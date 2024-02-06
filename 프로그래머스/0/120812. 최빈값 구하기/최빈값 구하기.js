function solution(array) {
    const counts = {};
    array.forEach((v) => {
        if (!counts[v]) counts[v] = 0;
        counts[v]++;
    })
    
    let mv = -1;
    let mk = -1;
    Object.entries(counts).forEach(([k, v]) => {
        if (v === mv) {
            mk = -1
        } else if (v > mv) {
            mk = k;
            mv = v;
        }
    })
    return +mk;
}