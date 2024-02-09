function solution(numbers) {
    const s = new Set([]);
    const l = numbers.length;
    for (let i=0; i<l-1; i++) {
        const n1 = numbers[i];
        for (let j=i+1; j<l; j++) {
            const n2 = numbers[j];
            s.add(n1+n2);
        }
    }
    return [...s].sort((a, b) => a-b);
}