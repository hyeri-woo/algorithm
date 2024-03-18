const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test2.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const [n, k] = input[0].split(" ").map((item) => parseInt(item));
  const dp = Array.from({ length: k + 1 }, () => Array(n + 1).fill(0));
  for (let i = 0; i <= n; i++) {
    dp[1][i] = 1;
    dp[2][i] = i + 1;
  }
  for (let i = 1; i <= k; i++) {
    dp[i][0] = 1;
    dp[i][1] = i;
  }
  for (let i = 3; i <= k; i++) {
    for (let j = 2; j <= n; j++) {
      dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
    }
  }
  return dp[k][n];
}

console.log(solution(input));
