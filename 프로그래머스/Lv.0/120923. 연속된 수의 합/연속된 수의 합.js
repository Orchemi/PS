function solution(num, total) {
    let result = []
    let start, end;
    if (num % 2) {
        const mid = total/num
        const partCount = (num-1)/2
        start = mid-partCount;
        end = mid+partCount;
    } else {
        const pairCount = num / 2
        const std = Math.trunc(total / num)
        start = std-(pairCount-1);
        end = std+(pairCount);
    }
    for (n=start; n<=end; n++) {
        result = [...result, n]
    }
    return result
}