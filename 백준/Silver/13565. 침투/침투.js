const fs = require("fs");
const input = fs
  .readFileSync('/dev/stdin')
  .toString()
  .split("\n")
  .map((a) => a.trim());

// 상하좌우 탐색
const delta = [
  [-1, 0],
  [1, 0],
  [0, -1],
  [0, 1],
];
const search = (i, j) => {
  for ([di, dj] of delta) {
    const [si, sj] = [i + di, j + dj];
    if (si < 0 || si >= I || sj < 0 || sj >= J) continue;
    if (mat[si][sj]) continue;
    mat[si][sj] = 2;
    if (si === I - 1) return true;
    if (search(si, sj)) return true;
  }
};

let ans = "NO";
const [I, J] = input[0].split(" ").map(Number);
const mat = [];
for (let i = 0; i < I; i++) {
  mat.push(input[i + 1].split("").map(Number));
}

for (let j = 0; j < J; j++) {
  if (!mat[0][j]) {
    mat[0][j] = 2;
    if (search(0, j)) {
      ans = "YES";
      break;
    }
  }
}

console.log(ans);