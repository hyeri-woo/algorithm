const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const dp = Array.from({ length: parseInt(input[0]) + 1 }, () =>
    Array(3).fill(0)
  );
  for (let i = 0; i < 3; i++) {
    dp[1][i] = 1;
  }
  for (let i = 2; i < dp.length; i++) {
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901;
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901;
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % 9901;
  }
  return dp[dp.length - 1].reduce((a, b) => a + b, 0) % 9901;
}

console.log(solution(input));
