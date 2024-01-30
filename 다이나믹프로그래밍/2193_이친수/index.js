const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const num = parseInt(input[0]);
  const dp = Array(num + 1).fill(0);
  dp[1] = 1;
  for (let i = 2; i < dp.length; i++) {
    dp[i] = BigInt(dp[i - 1]) + BigInt(dp[i - 2]);
  }
  return dp[dp.length - 1].toString();
}

console.log(solution(input));
