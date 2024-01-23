const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  let number = parseInt(input[0]);
  if (number === 0) return 0;
  const result = [];
  while (number !== 0) {
    result.push(Math.abs(number % -2));
    number = Math.ceil(number / -2);
  }
  return result.reverse().join("");
}

console.log(solution(input));
