function findOutputString(treeCount) {
  switch (treeCount) {
    case 0:
      return "No trees.";
    case 1:
      return "There is one tree.";
    default:
      return `A forest of ${treeCount} trees.`;
  }
}

function solution(input) {
  const data = input.map((arr) => arr.split(" ").map((v) => +v));
  const result = [];

  let cursor = 0;
  let caseNum = 1;

  // 모든 테스트 케이스 순회
  while (true) {
    const [N, E] = data[cursor];
    if (!N) break;

    // 연결노드 매핑 배열 만들기
    const edgeMap = [];
    for (let i = 0; i < N; i++) {
      edgeMap.push(new Array());
    }

    // 데이터마다 연결노드에 추가
    for (let i = 0; i < E; i++) {
      const [s, e] = data[i + cursor + 1];
      edgeMap[s - 1].push(e - 1);
      edgeMap[e - 1].push(s - 1);
    }

    let countTree = 0;
    const visited = Array(N).fill(0);

    // 재귀함수
    function visitChildren(parent, current) {
      visited[current] = 1;
      const children = edgeMap[current];

      let isCycle = false;
      children.forEach((c) => {
        if (c === parent) return;
        if (visited[c]) {
          isCycle = true;
          return;
        }

        const foundChildrenIsCycle = visitChildren(current, c);
        if (foundChildrenIsCycle) {
          isCycle = true;
        }
      });

      return isCycle;
    }

    // 데이터 -> 트리 조회 함수
    for (let i = 0; i < N; i++) {
      if (visited[i]) continue;
      const currentTreeCount = visitChildren(-1, i) ? 0 : 1;
      countTree += currentTreeCount;
    }

    // 후처리
    result.push(`Case ${caseNum}: ${findOutputString(countTree)}`);
    cursor += E + 1;
    caseNum++;
  }

  return result;
}

(function main() {
  let isLocal = false;
  let fs = require("fs");
  let filePath = isLocal ? "t.txt" : "/dev/stdin";
  let input = fs
    .readFileSync(filePath)
    .toString()
    .trim()
    .split("\n")
    .map((str) => str.trim());

  const answer = solution(input).join("\n");
  console.log(answer);
})();