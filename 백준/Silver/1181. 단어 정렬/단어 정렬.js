function solution(input) {
  const [_, ...list] = input;

  const itemSet = new Set(list);
  const lenSet = new Set([]);
  const map = {};

  [...itemSet].forEach((item) => {
    const l = String(item.length);

    if (lenSet.has(l)) {
      map[l].push(item);
    } else {
      map[l] = [item];
    }

    lenSet.add(l);
  });

  let result = [];
  const lenArr = [...lenSet].map((v) => +v).sort((a, b) => a - b);
  lenArr.forEach((l) => {
    const subArr = map[String(l)].sort((a, b) => (a > b ? 1 : -1));
    result = result.concat(subArr);
  });

  return result;
}

(function main() {
  let isLocal = false;
  let fs = require("fs");
  let filePath = isLocal ? "t.txt" : "/dev/stdin";
  let input = fs.readFileSync(filePath).toString().trim().split("\n");

  const answer = solution(input).join("\n");
  console.log(answer);
})();
