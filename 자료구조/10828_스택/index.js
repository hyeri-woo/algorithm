// const fs = require("fs");
// // TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
// const input = fs.readFileSync("test.txt").toString().trim().split("\n");

const readline = require("readline");
const fs = require("fs");

const rl = readline.createInterface({
  input: fs.createReadStream("test.txt"),
  output: process.stdout,
});

// 풀이
function solution(input) {
  const length = input[0];
  const stack = [];
  const answer = [];
  for (let i = 1; i <= length; i++) {
    const [prompt, number] = input[i].split(" ");
    if (prompt === "push") {
      stack.push(+number);
    } else if (prompt === "pop") {
      stack.length === 0 ? answer.push(-1) : answer.push(stack.pop());
    } else if (prompt === "size") {
      answer.push(stack.length);
    } else if (prompt === "empty") {
      stack.length === 0 ? answer.push(1) : answer.push(0);
    } else if (prompt === "top") {
      stack.length === 0
        ? answer.push(-1)
        : answer.push(stack[stack.length - 1]);
    }
  }
  return answer.join("\n");
}

const lines = [];
rl.on("line", function (line) {
  lines.push(line);
}).on("close", function () {
  console.log(solution(lines));
  process.exit(0);
});
