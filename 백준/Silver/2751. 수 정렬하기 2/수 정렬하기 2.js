function solution(input) {
  const [_, ...list] = input;
  return list.map((v) => +v).sort((a, b) => a - b);
}

(function main() {
  let isLocal = false;
  let fs = require("fs");
  let filePath = isLocal ? "t.txt" : "/dev/stdin";
  let input = fs.readFileSync(filePath).toString().trim().split("\n");

  const answer = solution(input).join("\n");
  console.log(answer);
})();
