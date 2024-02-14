const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const len = parseInt(input[0]);
  if (len % 2 === 1) return 0;
  const dp = Array(len + 1).fill(0);
  dp[0] = 1;
  dp[2] = 3;
  for (let i = 4; i < dp.length; i += 2) {
    dp[i] = dp[i - 2] * dp[2];
    for (let j = i - 4; j >= 0; j -= 2) {
      dp[i] += dp[j] * 2;
    }
  }
  return dp[dp.length - 1];
}

console.log(solution(input));
