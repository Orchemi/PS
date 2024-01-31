function solution(participant, completion) {
    const names = new Set(participant);
    const namesObj = {};
    names.forEach((n) => namesObj[n] = 0);
    
    participant.forEach((n) => namesObj[n]++);
    completion.forEach((n) => namesObj[n]--);
    return [...names].filter((n) => namesObj[n] > 0).at(0);
}