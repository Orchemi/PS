function solution(t, p) {
    const pl = p.length;
    const tl = t.length;
    const parts = [];
    for (i=0; i<tl-pl+1; i++) {
        const part = +t.slice(i, i+pl);
        parts.push(part);
    }
    
    const _p = +p;
    let ret = 0;
    parts.forEach((v) => v <= _p && ret++);
    return ret;
}