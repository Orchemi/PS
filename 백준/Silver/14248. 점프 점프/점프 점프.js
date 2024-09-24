function solution(input) {
  const N = Number(input[0]);
  const stones = input[1].split(" ").map(Number);
  const I = Number(input[2]) - 1;

  const visited = Array(N).fill(0);

  let trials = 0;
  let totalLength = 1;
  const queue = [I];
  visited[I] = 1;

  while (trials < totalLength) {
    const c = queue[trials];

    const move = stones[c];
    const prev = c - move;
    if (prev >= 0 && !visited[prev]) {
      visited[prev] = 1;
      totalLength++;
      queue.push(prev);
    }

    const next = c + move;
    if (next < N && !visited[next]) {
      visited[next] = 1;
      totalLength++;
      queue.push(next);
    }

    trials++;
  }

  return [visited.filter((v) => v).length];
}

(function main() {
  let isLocal = false;
  let fs = require("fs");
  let filePath = isLocal ? "t.txt" : "/dev/stdin";
  let input = fs.readFileSync(filePath).toString().trim().split("\n");

  const answer = solution(input).join("\n");
  console.log(answer);
})();