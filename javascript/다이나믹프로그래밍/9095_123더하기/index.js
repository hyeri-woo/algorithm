const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const numbers = input.map((n) => parseInt(n)).slice(1);
  const answer = [];
  const dp = Array(Math.max(...numbers) + 1).fill(0);
  dp[1] = 1;
  dp[2] = 2;
  dp[3] = 4;
  for (let i = 4; i < dp.length; i++) {
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
  }
  for (const n of numbers) {
    answer.push(dp[n]);
  }
  return answer.join("\n");
}

console.log(solution(input));
