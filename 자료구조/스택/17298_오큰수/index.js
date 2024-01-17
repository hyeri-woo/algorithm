const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test2.txt").toString().split("\n");

// 풀이
function solution(input) {
  const numbers = input[1].split(" ").map((item) => parseInt(item));
  const stack = [];
  const answer = Array(numbers.length).fill(-1);
  for (let i = 0; i < numbers.length; i++) {
    while (stack.length > 0 && numbers[stack[stack.length - 1]] < numbers[i]) {
      answer[stack.pop()] = numbers[i];
    }
    stack.push(i);
  }
  return answer.join(" ");
}

console.log(solution(input));
