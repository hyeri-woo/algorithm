const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const answer = [];
  for (let i = 1; i < input.length; i += 3) {
    const n = parseInt(input[i]);
    const numbers = [
      input[i + 1].split(" ").map((n) => parseInt(n)),
      input[i + 2].split(" ").map((n) => parseInt(n)),
    ];
    const dp = Array.from({ length: n + 1 }, () => Array(3).fill(0));
    dp[1][1] = numbers[0][0];
    dp[1][2] = numbers[1][0];
    for (let j = 2; j < dp.length; j++) {
      dp[j][0] = Math.max(...dp[j - 1]);
      dp[j][1] = Math.max(dp[j - 1][0], dp[j - 1][2]) + numbers[0][j - 1];
      dp[j][2] = Math.max(dp[j - 1][0], dp[j - 1][1]) + numbers[1][j - 1];
    }
    answer.push(Math.max(...dp[dp.length - 1]));
  }
  return answer.join("\n");
}

console.log(solution(input));
