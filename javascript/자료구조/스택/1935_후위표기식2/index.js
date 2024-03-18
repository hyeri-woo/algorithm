const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test1.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const char = input[1].split("");
  const stack = [];
  const value = [];
  for (let i = 2; i < parseInt(input[0]) + 2; i++) {
    value.push(parseInt(input[i]));
  }
  for (let i = 0; i < char.length; i++) {
    if (char[i] === "+") {
      stack.push(stack.pop() + stack.pop());
    } else if (char[i] === "-") {
      const second = stack.pop();
      const first = stack.pop();
      stack.push(first - second);
    } else if (char[i] === "*") {
      stack.push(stack.pop() * stack.pop());
    } else if (char[i] === "/") {
      const second = stack.pop();
      const first = stack.pop();
      stack.push(first / second);
    } else {
      stack.push(value[char[i].charCodeAt() - 65]);
    }
  }
  return stack[0].toFixed(2);
}

console.log(solution(input));
