const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split("\n")
  .map((a) => a.trim());

const main = (i) => {
    const N = +input[i*2+1]
    const arr = input[i*2+2].split(" ").map(Number);
    
    const red = [arr[0]];
    for (let j=1; j<N; j++) {
        red.push(red[j-1]+arr[j])
    }
    red.unshift(0)
    
    let maxx = arr[0]
    for (let s=0; s<N+1; s++) {
        for (let e=s+1; e<N+1; e++) {
            if (maxx < red[e]-red[s]) {
                maxx = red[e]-red[s]
            }
        }
    }
    return maxx
}

const T = +input[0]
for (let i=0; i<T; i++) {
    console.log(main(i))
}