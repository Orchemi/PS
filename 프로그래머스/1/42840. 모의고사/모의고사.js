function solution(answers) {
    const l = answers.length;
    const makeAnswers = (arr) => {
        const _ret = [];
        const _l = arr.length;
        const r = Math.ceil(l/_l);
        for (let i=0; i<r; i++) {
            _ret.push(...arr)
        }
        return _ret;
    };
    
    const a1 = makeAnswers([1, 2, 3, 4, 5]);
    const a2 = makeAnswers([2, 1, 2, 3, 2, 4, 2, 5]);
    const a3 = makeAnswers([3, 3, 1, 1, 2, 2, 4, 4, 5, 5]);
    
    let c1=0, c2=0, c3=0;
    answers.forEach((a, i) => {
        if (a1[i] === a) c1++;
        if (a2[i] === a) c2++;
        if (a3[i] === a) c3++;
    })
    
    const maxx = Math.max(c1, c2, c3);
    const ret = [];
    if (c1===maxx) ret.push(1);
    if (c2===maxx) ret.push(2);
    if (c3===maxx) ret.push(3);
    return ret;
}