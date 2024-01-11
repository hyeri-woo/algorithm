const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function solution(input) {
  const [a, b] = input[0].split(" ");
  return Number(a) + Number(b);
}

const lines = [];
rl.on("line", function (line) {
  lines.push(line);
}).on("close", function () {
  console.log(solution(lines));
  process.exit(0);
});
