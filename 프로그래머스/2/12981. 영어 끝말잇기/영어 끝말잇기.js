function solution(n, words) {
    const did = new Set();
    let prevChar = words[0][0];
    for (let round=0; round>=0; round++) {
        for (let num=0; num<n; num++) {
            const word = words[round*n + num];
            if (!word) return [0, 0];
            if (did.has(word) || !word.startsWith(prevChar)) return [num+1, round+1];
            did.add(word);
            prevChar = word.at(-1);
        }
    }
}