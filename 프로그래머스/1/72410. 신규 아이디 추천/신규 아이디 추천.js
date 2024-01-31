function solution(new_id) {
    let ret = new_id;
    
    ret = ret.toLowerCase();
    ret = Array.from(ret).filter((c) => {
        const cc = c.charCodeAt();
        if (97 <= cc && cc <= 122 ) return true;
        if (Number.isInteger(Number(c))) return true;
        return new Set(['-', '_', '.']).has(c);
    }).join('');
    
    ret = ret.split('.').filter(v => v).join('.');
    if (!ret) ret = 'a';
    if (ret.length >= 16) ret = ret.slice(0, 15);
    if (ret.endsWith('.')) ret = ret.slice(0, ret.length-1);
    let l = ret.length;
    if (l <= 2) ret += ret[l-1].repeat(3-l);
    return ret;
}