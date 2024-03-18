const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test2.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const numbers = input[1].split(" ").map((n) => parseInt(n));
  const dp = Array(numbers.length).fill(0);
  dp[0] = numbers[0];
  for (let i = 1; i < dp.length; i++) {
    dp[i] = Math.max(dp[i - 1] + numbers[i], numbers[i]);
  }
  return Math.max(...dp);
}

console.log(solution(input));
