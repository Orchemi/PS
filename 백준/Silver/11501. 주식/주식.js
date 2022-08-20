const fs = require("fs");
const input = fs
  .readFileSync('/dev/stdin')
  .toString()
  .split("\n")
  .map((a) => a.trim());

const foo = (i) => {
  const N = +input[2 * i + 1];
  const arr = input[2 * i + 2].split(" ").map(Number);
  let k = N - 1;
  let maxx = arr[k];
  let ssum = 0;
  while (k >= 0) {
    if (maxx < arr[k]) {
      maxx = arr[k];
    } else {
      ssum += maxx - arr[k];
    }
    k--;
  }
  return ssum;
};

const T = +input[0];
for (let i = 0; i < T; i++) {
  console.log(foo(i));
}