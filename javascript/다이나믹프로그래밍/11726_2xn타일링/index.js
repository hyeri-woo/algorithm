const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test2.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const dp = Array(parseInt(input[0]) + 1).fill(0);
  dp[1] = 1;
  dp[2] = 2;
  for (let i = 3; i < dp.length; i++) {
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007;
  }
  return dp[dp.length - 1];
}

console.log(solution(input));
