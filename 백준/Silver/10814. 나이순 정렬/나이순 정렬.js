function solution(input) {
  const [_, ...arrs] = input;

  const data = arrs.map((arr) => {
    const [age, name] = arr.split(" ");
    return [+age, name];
  });

  const result = data.sort((a, b) => a[0] - b[0]);

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
