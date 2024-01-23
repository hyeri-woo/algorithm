const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const number = input[0].split("").map((n) => parseInt(n));
  const answer = [];
  answer.push(number[0].toString(2));
  for (let i = 1; i < number.length; i++) {
    answer.push(number[i].toString(2).padStart(3, "0"));
  }
  return answer.join("");
}

console.log(solution(input));
