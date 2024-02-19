

function solution(number, limit, power) {
    const numsList = new Array(number+1).fill(1);
    for (let i=2; i<=number; i++) {
        for (let j=i; j<=number; j+=i) {
            numsList[j]++;
        }
    }
    return numsList.map((n) => n > limit ? power : n).reduce((a, c) => a+c) - 1;
}