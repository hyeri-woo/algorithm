const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test2.txt").toString().split("\n");

// 풀이
function solution(input) {
  const inputs = input[0];
  const container = [];
  let answer = 0;
  let index = 0;
  while (index < inputs.length) {
    if (inputs.slice(index, index + 2) === "()") {
      answer += container.length;
      index++;
    } else if (inputs[index] === ")") {
      container.pop();
      answer++;
    } else {
      container.push("(");
    }
    index++;
  }
  return answer;
}

console.log(solution(input));
