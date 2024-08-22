function solution(input) {
  let count = Number(input[0]);
  let arr = [];
  let str = "";
  for (let i = 1; i <= count; i++) {
    arr.push(Number(input[i]));
  }

  arr.sort((a, b) => a - b);
  for (let i = 0; i < arr.length; i++) {
    str += arr[i] + "\n";
  }
  console.log(str);
}

(function main() {
  let isLocal = false;
  let fs = require("fs");
  let filePath = isLocal ? "t.txt" : "/dev/stdin";
  let input = fs.readFileSync(filePath).toString().split("\n");
  solution(input);
})();
