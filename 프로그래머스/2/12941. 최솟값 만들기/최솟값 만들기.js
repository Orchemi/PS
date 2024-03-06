function solution(A,B){
    const l = A.length;
    const _A = A.sort((a, b) => b-a);
    const _B = B.sort((a, b) => a-b);
    
    let ret = 0;
    for (let i=0; i<l; i++) {
        ret += _A[i]*_B[i];
    }
    return ret;
}