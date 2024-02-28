function solution(s, n) {
    return Array.from(s).map((c) => {
        if (c === ' ') return ' ';
        
        const cc = c.charCodeAt();
        const isUpperCase = 'a'.charCodeAt() > cc;
        
        let ccn = cc+n;
        if (isUpperCase) {
            if (ccn > 'Z'.charCodeAt()) ccn -= 26;
        } else {
            if (ccn > 'z'.charCodeAt()) ccn -= 26;
        }
        
        return String.fromCharCode(ccn);
    }).join('');
}