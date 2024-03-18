const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const numbers = input[0].split(" ");
  const answer = [];
  for (let i = 0; i < numbers.length - 1; i += 2) {
    answer.push(numbers[i] + numbers[i + 1]);
  }
  return answer.reduce((a, b) => a + parseInt(b), 0);
}

console.log(solution(input));
