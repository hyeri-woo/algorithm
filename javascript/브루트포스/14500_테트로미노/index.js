const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test1.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const paper = [];
  const [n, m] = input[0].split(" ").map(Number);
  for (let i = 1; i < input.length; i++) {
    paper.push(input[i].split(" ").map(Number));
  }

  const dfs = (paper, start) => {
    const checked = Array.from({ length: n }, () => Array(m).fill(false));
    const stack = [];
    stack.push(start);
    let max = 0;
    for (let i = 0; i < 3; i++) {
      const [x, y] = stack.pop();
      if(!checked[x][y]) {
        checked[x][y] = true;
        stack.push([x, y]);
      }
    }
  };

  //   for (let i = 0; i < paper.length; i++) {
  //     for (let j = 0; j < paper[0].length; i++) {}
  //   }

  return paper;
}

console.log(solution(input));
