function solution(babbling) {
    const possibleBabblings = ["aya", "ye", "woo", "ma"];
    const checkBab = (bab) => {
        let ret = bab;
        let prevBabbling = '';
        for (let i=0; i<4; i++) {
            const b = possibleBabblings[i];
            if (!ret.startsWith(b)) continue;
            if (b === prevBabbling) continue;
            ret = ret.replace(b, '');
            prevBabbling = b;
            i = -1;
        }
        return !ret;
    }
    return babbling.filter((bab) => checkBab(bab)).length;
}