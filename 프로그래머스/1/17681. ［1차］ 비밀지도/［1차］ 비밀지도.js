function solution(n, arr1, arr2) {
    const convertToBin = (arr) => arr.map((l) => l.toString(2).padStart(n, '0'));
    const b1 = convertToBin(arr1);
    const b2 = convertToBin(arr2);
    
    const ret = [];
    for (let i=0; i<n; i++) {
        let line = '';
        for (let j=0; j<n; j++) {
            line += b1[i][j]|b2[i][j] ? '#' : ' ';
        }
        ret.push(line);
    }
    return ret;
}