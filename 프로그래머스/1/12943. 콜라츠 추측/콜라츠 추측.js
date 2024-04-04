function solution(num) {
    let count = 0;
    for (let n=0; n<500; n++) {
        if (num===1) break;
        if (num%2) {
            num = num*3+1;
        } else {
            num = num/2;
        }
        count++;
    }
    
    return count === 500 ? -1 : count;
}