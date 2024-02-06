const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const n = parseInt(input[0]);
  const dp = input
    .slice(1)
    .map((item) => item.split(" ").map((n) => parseInt(n)));
  for (let i = 0; i < n; i++) {
    while (dp[i].length < n) {
      dp[i].push(0);
    }
  }

  for (let i = 1; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (j === 0) dp[i][j] += dp[i - 1][j];
      else dp[i][j] += Math.max(dp[i - 1][j], dp[i - 1][j - 1]);
    }
  }
  return Math.max(...dp[dp.length - 1]);
}

console.log(solution(input));
