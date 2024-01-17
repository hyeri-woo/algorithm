const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test5.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const chars = input[0].split("");
  const stack = [];
  const answer = [];
  for (let i = 0; i < chars.length; i++) {
    const char = chars[i];
    if (char === "(") {
      stack.push(char);
    } else if (char === ")") {
      while (stack.length && stack[stack.length - 1] !== "(") {
        answer.push(stack.pop());
      }
      stack.pop();
    } else if (char === "*" || char === "/") {
      while (
        (stack.length && stack[stack.length - 1] === "*") ||
        stack[stack.length - 1] === "/"
      ) {
        answer.push(stack.pop());
      }
      stack.push(char);
    } else if (char === "+" || char === "-") {
      while (stack.length && stack[stack.length - 1] !== "(") {
        answer.push(stack.pop());
      }
      stack.push(char);
    } else {
      answer.push(char);
    }
  }
  while (stack.length) {
    answer.push(stack.pop());
  }
  return answer.join("");
}

console.log(solution(input));
