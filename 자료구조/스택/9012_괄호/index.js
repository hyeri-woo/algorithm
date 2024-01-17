const readline = require("readline");
const fs = require("fs");

const rl = readline.createInterface({
  input: fs.createReadStream("test2.txt"),
  output: process.stdout,
});

// 풀이
function solution(input) {
  const answer = [];
  for (let i = 1; i <= input[0]; i++) {
    const vps = [];
    const cases = input[i].split("");
    for (let j = 0; j < cases.length; j++) {
      if (cases[j] === "(") {
        vps.push("(");
      } else if (cases[j] === ")" && vps[vps.length - 1] === "(") {
        vps.pop();
      } else {
        vps.push(")");
      }
    }
    if (vps.length === 0) answer.push("YES");
    else answer.push("NO");
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
