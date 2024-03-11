function solution(k, score) {
    const honors = [];
    const ret = [];
    score.forEach((s, i) => {
        honors.push(s);
        honors.sort((a, b) => b-a);
        ret.push(honors[Math.min(i, k-1)]);
    })
    return ret;
}