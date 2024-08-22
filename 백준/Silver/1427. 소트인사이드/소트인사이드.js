function solution(input) {
  const arr = input[0].split("");
  return [arr.sort((a, b) => (a < b ? 1 : -1)).join("")];
}

(function main() {
  let isLocal = false;
  let fs = require("fs");
  let filePath = isLocal ? "t.txt" : "/dev/stdin";
  let input = fs.readFileSync(filePath).toString().trim().split("\n");

  const answer = solution(input).join("\n");
  console.log(answer);
})();