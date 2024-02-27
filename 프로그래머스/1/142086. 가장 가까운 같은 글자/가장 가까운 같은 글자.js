function solution(s) {
    const l = s.length;
    const ret = new Array(l).fill(-1);
    const lastIdxs = {};
    
    for (let i=l-1; i>=0; i--) {
        const c = s[i];
        const lastIdx = lastIdxs[c];
        if (lastIdx) {
            ret[lastIdx] = lastIdx - i;
        }
        lastIdxs[c] = i;
    }
    return ret;
}