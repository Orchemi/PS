const findNextChar = (c) => {
    return c === 'z' ? 'a' : String.fromCharCode(c.charCodeAt() + 1);
}

function solution(s, skip, index) {
    const findSkippedNextChar = (currentChar) => {
        let ret = findNextChar(currentChar);
        while (skip.includes(ret)) {
            ret = findNextChar(ret);
        }
        return ret;
    }
    
    const jump = (c) => {
        let ret = c;
        let count = 0;
        while (count < index) {
            count++;
            ret = findSkippedNextChar(ret);
        }
        return ret;
    }
    
    return s.split('').map((c) => jump(c)).join('');
}