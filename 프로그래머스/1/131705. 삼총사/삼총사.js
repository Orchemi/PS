function solution(number) {
    const l = number.length;
    let ret = 0;
    for (i1=0; i1<l-2; i1++){
        const n1 = number[i1];
        for (i2=i1+1; i2<l-1; i2++) {
            const n2 = number[i2];
            for (i3=i2+1; i3<l; i3++) {
                const n3 = number[i3];
                console.log(n1, n2, n3, n1+n2+n3);
                if (n1+n2+n3 === 0) ret++;
            }
        }
    }
    return ret;
}