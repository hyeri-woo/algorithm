const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const numbers = input[1].split(" ").map((n) => parseInt(n));
  const dp = Array.from({ length: 2 }, () => Array(parseInt(input[0])).fill(0));
  let max = numbers[0];
  dp[0][0] = numbers[0];
  for (let i = 1; i < dp[0].length; i++) {
    dp[0][i] = Math.max(dp[0][i - 1] + numbers[i], numbers[i]);
    dp[1][i] = Math.max(dp[1][i - 1] + numbers[i], dp[0][i - 1]);
    max = Math.max(max, dp[0][i], dp[1][i]);
  }
  return max;
}

console.log(solution(input));
