const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test2.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const mod = 1000000000;
  const num = parseInt(input[0]);
  const dp = Array.from({ length: num + 1 }, () => Array(10).fill(0));
  for (let i = 1; i < 10; i++) {
    dp[1][i] = 1;
  }
  for (let i = 2; i < dp.length; i++) {
    for (let j = 0; j < 10; j++) {
      if (j === 0) {
        dp[i][j] = dp[i - 1][j + 1] % mod;
      } else if (j === 9) {
        dp[i][j] = dp[i - 1][j - 1] % mod;
      } else {
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % mod;
      }
    }
  }
  return dp[dp.length - 1].reduce((a, b) => a + b, 0) % mod;
}

console.log(solution(input));
