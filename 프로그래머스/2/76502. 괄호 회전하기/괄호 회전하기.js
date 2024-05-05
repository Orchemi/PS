function solution(s) {
    const PAIR = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    const OPENS = new Set(Object.values(PAIR));
    
    const check = (s) => {
        const stack = [];
        let sl = -1;
        for (let i=0; i<s.length; i++) {
            const c = s[i];
            
            if (OPENS.has(c)) {
                stack.push(c);
                sl++;
            } else {
                if (sl < 0) return false;
                if (stack[sl] !== PAIR[c]) return false;
                stack.pop();
                sl--;
            }
        }
        return sl < 0;
    }
    
    const l = s.length;
    let count = 0;
    for (let i=0; i<l; i++) {
        const newS = s.slice(i) + s.slice(0, i);
        count += check(newS) ? 1 : 0;
    }
    
    return count;
}