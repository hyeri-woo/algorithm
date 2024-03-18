const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test1.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  let number = parseInt(input[0]);
  let divisor = 2;
  const answer = [];
  while (number > 1) {
    if (number % divisor === 0) {
      answer.push(divisor);
      number = number / divisor;
    } else divisor++;
  }
  return answer.join("\n");
}

console.log(solution(input));
