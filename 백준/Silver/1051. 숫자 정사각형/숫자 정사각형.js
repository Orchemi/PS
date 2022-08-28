const fs = require("fs");
const [IJ, ...mat] = fs
  .readFileSync('/dev/stdin')
  .toString()
  .split("\n")
  .map((a) => a.trim());

mat.forEach((line) => line.split(""));

const check = (L) => {
  for (let i = 0; i + L < I; i++) {
    for (let j = 0; j + L < J; j++) {
      if (
        [mat[i + L][j], mat[i][j + L], mat[i + L][j + L]].every(
          (point) => point === mat[i][j]
        )
      )
        return true;
    }
  }
};

const [I, J] = IJ.split(" ").map(Number);
let ret = 1;
for (let L = Math.min(I, J) - 1; L > 0; L--) {
  if (check(L)) {
    ret = L + 1;
    break;
  }
}
console.log(ret ** 2);