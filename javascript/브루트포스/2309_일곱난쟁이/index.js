const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const heights = input.map((n) => parseInt(n));
  for (let i = 0; i < heights.length; i++) {
    for (let j = i + 1; j < heights.length; j++) {
      const answer = [...heights].filter(
        (_, index) => index !== i && index !== j
      );
      if (answer.reduce((a, b) => a + b, 0) === 100) {
        answer.sort((a, b) => a - b);
        return answer.join("\n");
      }
    }
  }
}

console.log(solution(input));
