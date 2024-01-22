const divide = (N) => {
    const ret = new Array(10).fill(0);
    N.split('').forEach((n) => {
        ret[Number(n)]++;
    })
    return ret;
}
function solution(X, Y) {
    const parts1 = divide(X);
    const parts2 = divide(Y);
    const minList = [];
    for (i=0; i<10; i++) {
        minList.push(Math.min(parts1[i], parts2[i]));
    }
    
    let ret = '';
    for (i=9; i>=0; i--) {
        ret += `${i}`.repeat(minList[i]);
    }
    return !ret ? '-1' : !ret.replaceAll('0', '') ? '0' : ret;
}