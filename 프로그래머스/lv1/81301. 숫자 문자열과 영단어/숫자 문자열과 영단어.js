function solution(s) {
    const number = new Set(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
    const ston = {
        "zero": '0',
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9'
    }
    
    const sl = s.length;
    let ans = ''
    let i = 0;
    while (i < sl){
        let c = s[i]
        if (number.has(c)) {
            ans += c
            i++;
        } else {
            tmp = ''
            while (i < sl){
                c = s[i]
                if (!number.has(c)) {
                    tmp += c
                    if (ston[tmp]) {
                        ans += ston[tmp]
                        tmp = ''
                    }
                    i++;    
                } else {
                    break;
                }
            }
            if (i===sl && ston[tmp]) {
                ans += ston[tmp]
            }
        }
    }
    return +ans;
}