const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test1.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  let answer = 0;
  let number = parseInt(input[0]);
  while (number > 0) {
    answer += parseInt(number / 5);
    number = parseInt(number / 5);
  }
  return answer;
}

console.log(solution(input));
