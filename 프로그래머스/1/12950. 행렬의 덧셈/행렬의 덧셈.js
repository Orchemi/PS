function solution(arr1, arr2) {
    const l1 = arr1.length;
    const l2 = arr1[0].length;
    const ret = [];
    for (let i=0; i<l1; i++) {
        ret.push([]);
        for (let j=0; j<l2; j++) {
            ret[i].push(arr1[i][j] + arr2[i][j]);
        }
    }
    return ret;
}