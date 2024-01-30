function solution(absolutes, signs) {
    let ret = 0;
    const l = signs.length;
    for (i=0; i<l; i++) {
        const v = absolutes[i];
        ret += signs[i] ? v : -v;
    }
    return ret;
}