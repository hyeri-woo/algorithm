const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test2.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const dp = Array(parseInt(input[0]) + 1).fill(0);
  for (let i = 2; i < dp.length; i++) {
    if (i % 3 === 0 && i % 2 === 0) {
      dp[i] = Math.min(dp[i / 3], dp[i / 2], dp[i - 1]) + 1;
    } else if (i % 3 === 0) {
      dp[i] = Math.min(dp[i / 3], dp[i - 1]) + 1;
    } else if (i % 2 === 0) {
      dp[i] = Math.min(dp[i / 2], dp[i - 1]) + 1;
    } else {
      dp[i] = dp[i - 1] + 1;
    }
  }
  return dp[dp.length - 1];
}

console.log(solution(input));
