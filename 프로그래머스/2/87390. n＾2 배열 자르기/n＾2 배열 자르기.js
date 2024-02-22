function solution(n, left, right) {
    const ret = [];
    let currentI = Math.trunc((left-1)/n)
    let currentJ = left - currentI*n;
    let currentIdx = left;
    while (currentIdx <= right) {
        const currentNum = currentJ >= currentI+1 ? currentJ+1 : currentI+1;
        ret.push(currentNum);
        if (currentJ === n-1) {
            currentI++;
            currentJ = 0;
        } else {
            currentJ++;
        }
        currentIdx++;
    }
    return ret;
}