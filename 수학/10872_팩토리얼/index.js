const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test1.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const num = parseInt(input[0]);
  const factorial = (n) => (n === 0 ? 1 : n * factorial(n - 1));
  return factorial(num);
}

console.log(solution(input));
