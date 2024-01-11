const fs = require("fs");

const input = fs.readFileSync("test2.txt").toString().trim().split("\n");
// const input = fs.readFileSync("test2.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const stack = [];
  const answer = [];
  let now = 1;
  for (let i = 1; i <= input[0]; i++) {
    const target = parseInt(input[i]);
    while (now <= target) {
      stack.push(now);
      answer.push("+");
      now++;
    }
    if (stack[stack.length - 1] === target) {
      stack.pop();
      answer.push("-");
    }
  }

  if (stack.length !== 0) return "NO";
  else return answer.join("\n");
}

console.log(solution(input));
