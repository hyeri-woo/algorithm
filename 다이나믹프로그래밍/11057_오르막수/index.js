const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test3.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const dp = Array.from({ length: parseInt(input) + 1 }, () =>
    Array(10).fill(0)
  );
  for (let i = 0; i < 10; i++) {
    dp[1][i] = 1;
  }
  for (let i = 0; i <= parseInt(input); i++) {
    dp[i][0] = 1;
  }
  for (let i = 2; i < dp.length; i++) {
    for (let j = 1; j < 10; j++) {
      dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 10007;
    }
  }
  return dp[dp.length - 1].reduce((a, b) => a + b, 0) % 10007;
}

console.log(solution(input));
