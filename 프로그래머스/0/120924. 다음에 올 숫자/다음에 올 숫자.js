const checkDB = (lst) => {
    const l = lst.length;
    const db = lst[1] / lst[0];
    
    for (i=1; i<l; i++) {
        if (lst[i] !== lst[i-1] * db) return [false, db];
    }
    return [true, lst[l-1] * db];
}

const checkDC = (lst) => {
    const l = lst.length;
    const dc = lst[1] - lst[0];
    
    for (i=1; i<l; i++) {
        if (lst[i] !== lst[i-1] + dc) return [false, dc];
    }
    return [true, lst[l-1] + dc];
}

function solution(common) {
    const l = common.length;
    const [dcValid, dcRet] = checkDC(common);
    if (dcValid) return dcRet;
    const [dbValid, dbRet] = checkDB(common);
    return dbRet;
}