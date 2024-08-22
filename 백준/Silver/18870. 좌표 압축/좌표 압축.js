function solution(input) {
  const list = input[1].split(" ");

  // list를 set 처리하여 중복을 제거한다.
  const set = new Set(list);

  // set을 list 치환하여 오름차순 정렬한다.
  const sortedList = [...set].map((v) => +v).sort((a, b) => a - b);

  // 각 개수의 누적값을 저장하는 obj를 만든다.
  const countObj = {};
  sortedList.forEach((v, i) => (countObj[v] = i));

  // list를 순회하며 obj의 key에 해당하는 값을 반환한다.
  const result = list.map((v) => countObj[v]).join(" ");
  return [result];
}

(function main() {
  let isLocal = false;
  let fs = require("fs");
  let filePath = isLocal ? "t.txt" : "/dev/stdin";
  let input = fs.readFileSync(filePath).toString().trim().split("\n");

  const answer = solution(input).join("\n");
  console.log(answer);
})();
