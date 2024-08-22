function solution(input) {
  const K = +input[0].split(" ")[1];
  const nums = input[1].split(" ").map((v) => +v);
  const sortedNums = nums.sort((a, b) => a - b);
  return [sortedNums[+K - 1]];
}

(function main() {
  let isLocal = false;
  let fs = require("fs");
  let filePath = isLocal ? "t.txt" : "/dev/stdin";
  let input = fs.readFileSync(filePath).toString().trim().split("\n");

  const answer = solution(input).join("\n");
  console.log(answer);
})();
