const readline = require("readline");
const fs = require("fs");

const rl = readline.createInterface({
  input: fs.createReadStream("test.txt"),
  output: process.stdout,
});

// 풀이
function solution(input) {
  const [a, b] = input.split(" ");
  return Number(a) + Number(b);
}

const lines = [];
rl.on("line", function (line) {
  lines.push(line);
}).on("close", function () {
  console.log(solution(lines));
  process.exit(0);
});
