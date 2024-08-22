function solution(input) {
  const [_, ...arrs] = input;
  const orders = {};

  const data = arrs.map((arr, i) => {
    orders[arr] = i;
    const _arr = arr.split(" ");
    _arr[0] = +_arr[0];
    return _arr;
  });

  const result = data.sort((a, b) => {
    const [age1, name1] = a;
    const [age2, name2] = b;
    return age1 === age2 ? orders[name1] - orders[name2] : age1 - age2;
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