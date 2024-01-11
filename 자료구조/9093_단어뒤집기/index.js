const readline = require("readline");
const fs = require("fs");

const rl = readline.createInterface({
  input: fs.createReadStream("test.txt"),
  output: process.stdout,
});

function solution(input) {
  const answer = [];
  for (let i = 1; i < input.length; i++) {
    const innerAnswer = [];
    for (const word of input[i].split(" ")) {
      innerAnswer.push(word.split("").reverse().join(""));
    }
    answer.push(innerAnswer.join(" "));
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
