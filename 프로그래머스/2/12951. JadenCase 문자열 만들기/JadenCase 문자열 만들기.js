function solution(s) {
    let ret = s;
    ret = ret.toLowerCase();
    const lst = ret.split(' ');
    return lst.map((v) => {
        if (!v) return v;
        let l = Array.from(v);
        l[0] = l[0].toUpperCase();
        return l.join('');
    }).join(' ');
}