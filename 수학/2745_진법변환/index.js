const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const [number, bin] = input[0].split(" ");
  return parseInt(number, bin);
}

console.log(solution(input));
