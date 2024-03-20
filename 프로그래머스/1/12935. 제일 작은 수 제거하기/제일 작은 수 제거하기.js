function solution(arr) {
    const min = Math.min(...arr);
    const ret = arr.filter((n) => n !== min);
    return ret.length > 0 ? ret : [-1];
}