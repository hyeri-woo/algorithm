const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("test6.txt").toString().trim().split("\n");

// 풀이
function solution(input) {
  const dp = Array(parseInt(input[0]) + 1).fill(0);
  const cards = input[1].split(" ").map((n) => parseInt(n));
  for (let i = 0; i < cards.length; i++) {
    dp[i + 1] = cards[i];
  }
  for (let i = 2; i < dp.length; i++) {
    let min = dp[i];
    for (let j = 0; j <= i / 2; j++) {
      if (dp[j] + dp[i - j] < min) {
        min = dp[j] + dp[i - j];
      }
    }
    dp[i] = min;
  }
  return dp[dp.length - 1];
}

console.log(solution(input));
