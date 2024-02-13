const findNextRet = (n) => {
    let ret = n+1;
    while (true) {
        if (ret%3 === 0 || `${ret}`.includes('3')) {
            ret++;
            continue;
        } 
        return ret;
    }
};

function solution(n) {
    let cnt = 1;
    let ret = 1;
    while (cnt < n) {
        ret = findNextRet(ret);
        cnt++;
    }
    return ret;
}