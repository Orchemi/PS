function solution(s){
    let sl = 0;
    
    for (i=0; i<s.length; i++) {
        if (s[i] === '(') {
            sl++;
            continue;
        }
        
        if (!sl) return false;
        sl--;
        }
    return sl ? false : true;
}