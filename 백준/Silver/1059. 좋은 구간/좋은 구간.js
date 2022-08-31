const fs = require("fs");
const [L, two, n] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split("\n")
  .map((a) => a.trim());

const arr = two.split(" ").map(Number);
const maxx = Math.max(...arr);

const S = new Set(arr);
let cnt = 0;
for (let s = 1; s < maxx + 1; s++) {
  if (s > n) break;
  if (S.has(s)) continue;
  for (let e = s + 1; e < maxx + 1; e++) {
    if (S.has(e)) break;
    if (e < n) continue;
    cnt++;
  }
}
console.log(cnt);