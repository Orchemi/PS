function solution(input) {
  const [_, ...arrs] = input;
  const data = arrs.map((arr) => arr.split(" ").map((v) => +v));

  const result = data.sort((a, b) => {
    const [x1, y1] = a;
    const [x2, y2] = b;
    return x1 === x2 ? y1 - y2 : x1 - x2;
  });

  return result.map((arr) => arr.join(" "));
}

(function main() {
  let isLocal = false;
  let fs = require("fs");
  let filePath = isLocal ? "t.txt" : "/dev/stdin";
  let input = fs.readFileSync(filePath).toString().trim().split("\n");

  const answer = solution(input).join("\n");
  console.log(answer);
})();