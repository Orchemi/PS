function solution(s) {
    const l = s.length;
    let ret = 0;
    let firstChar = s[0];
    let counts = [0, 0];
    
    for (i=0; i<l; i++) {
        const currentChar = s[i];
        counts[currentChar === firstChar ? 0 : 1]++;
        if (counts[0] === counts[1]) {
            ret++;
            counts = [0, 0];
            if (i+1 === l) break;
            firstChar = s[i+1];  
        };
    };
    
    return counts.reduce((a, b) => a+b, 0) ? ret+1 : ret;
}