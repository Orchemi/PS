const fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split("\n")
  .map((a) => a.trim());

const [N, M] = input[0].split(" ").map(Number);
const minn = [1e10, 1e10];
for (let i = 0; i < M; i++) {
  const [six, one] = input[i + 1].split(" ").map(Number);
  minn[0] = Math.min(minn[0], six);
  minn[1] = Math.min(minn[1], one);
}

const allOne = N * minn[1];
const sixAndOne =
  Math.floor(N / 6) * minn[0] + (N - Math.floor(N / 6) * 6) * minn[1];
const allSix = Math.ceil(N / 6) * minn[0];
console.log(Math.min(allOne, sixAndOne, allSix));