const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split("\n")
  .map((a) => a.trim());

let [N, K] = input[0].split(" ").map(Number);
const obj = {};
for (let i = 0; i < N; i++) {
  const n = input[i + 1];
  obj[n] = obj[n] ? obj[n] + 1 : 1;
}

const levels = Object.keys(obj)
  .map(Number)
  .sort((a, b) => a - b);

const ll = levels.length;
let sames = obj[levels[0]];
let ret = +levels[0];
let i = 0;

while (K > 0 && i < ll && sames * (levels[i + 1] - levels[i]) <= K) {
  K -= sames * (levels[i + 1] - levels[i]);
  sames += obj[levels[i + 1]];
  ret = levels[i + 1];
  i++;
}

ret += Math.floor(K / sames);
console.log(ret);