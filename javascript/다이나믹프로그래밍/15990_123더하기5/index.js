const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const MOD = 1000000009;
  const numbers = input.map((n) => parseInt(n)).slice(1);
  const answer = [];
  const dp = Array.from({ length: Math.max(...numbers) + 1 }, () => [
    0, 0, 0, 0,
  ]);
  dp[1][1] = 1;
  dp[2][2] = 1;
  dp[3][1] = 1;
  dp[3][2] = 1;
  dp[3][3] = 1;
  for (let i = 4; i < dp.length; i++) {
    dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % MOD;
    dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % MOD;
    dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % MOD;
  }
  for (const n of numbers) {
    answer.push((dp[n][1] + dp[n][2] + dp[n][3]) % MOD);
  }
  return answer.join("\n");
}

console.log(solution(input));
