// function solution(d, budget) {
//     d.sort();
//     let cnt = 0;
//     for (let i=0; i<d.length; i++) {
//         const n = d[i];
//         if (budget < n) return cnt;
//         budget -= n;
//         cnt++;
//     }
//     return cnt;
// }

function solution(d, budget) {
    var answer = 0;
    var total = 0;

    d.sort((a, b) => a - b).forEach(price => {
        if(total + price <= budget) {
            total += price; 
            answer++;
        }
    });

    return answer;
}