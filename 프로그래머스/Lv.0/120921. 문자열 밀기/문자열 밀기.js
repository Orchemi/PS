const push = (str) => {
    const l = str.length;
    return str[l-1] + str.slice(0, l-1);
}

function solution(A, B) {
    let tmp = A;
    let count = -1;
    for (i = 0; i < A.length; i++) {
        if (tmp === B) {
            count = i;
            break;
        }
        tmp = push(tmp)
    }
    return count;
}