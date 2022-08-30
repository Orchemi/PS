function solution(survey, choices) {
    const scores = {}
    
    survey.forEach((item, idx) => {
        const num = choices[idx]-4
        const [left, right] = item.split("")
        if (num < 0) {
            scores[left] ? (scores[left] -= num) : scores[left] = -num;
        } else if (num > 0) {
            scores[right] ? (scores[right] += num) : scores[right] = num;
        }
    })
    
    let ans = ''
    const check = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    check.forEach((ch) => {
        const [l, r] = ch;
        const n1 = scores[l] ? scores[l] : 0
        const n2 = scores[r] ? scores[r] : 0
        const ret = n1 < n2 ? r : l
        ans += ret
    })
    return ans;
}