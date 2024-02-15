function solution(k, m, score) {
    let ret = 0;
    score.sort((a, b) => b-a);
    for (let bi=0; bi<Math.trunc(score.length/m); bi++) {
        ret += score[bi*m+(m-1)]*m;
    }
    return ret;
}